#!/usr/bin/env python

""" This file and repository is an example use case for using Tesuto validation and emulation for
each time a configuration file is changed. This file is designed for use with gitlab-ci but the
conventions outlined are applicable to most all CI environments with minor modifications.

REQUIRED ENVIRONMENT VARIABLE:

    AUTH_TOKEN: Required API authentcation token. For use with Gitlab, this can be configured
                as a secret variable in the repository configuration.

OPTIONAL ENVIRONMENT VARIABLES:

    API_URL: An optional url and should only be set for dev purposes.
    CI_JOB_ID: Dynamically set by Gitlab-CI. It is the unique CI job id and is used as a unique
               emulation name. If not running in Gitlab and this value is not present, the
               current epoch timestamp will be used for the emulation name. Can be overridden by
               environment value.
    TIMEOUT: The default timeout for a CI process time is 15 minutes. This can be overriden
             with by setting the timeout value in seconds.
    CHECK_INTERVAL: How often to poll the JOB API for job status updates. Defaults to 30 seconds.
    DELETE_EMULATION: Auto delete the emulation on success. Default is false.

REQUIRED FILES:

    devices.yaml: Containts the device name, version, and interface config
    topologies.yaml: Contains topology configuration
    validators.yaml: Contains script name, parse_params, state_params.

REQUIRED MODULES:

    pip install requests PyYAML

IMPORTANT NOTES:

    The timeout default is 15 minutes. Depending on size of emulation and number of validators
    this value may need to be increased.
"""

import json
import os
import sys
import requests
import time
import yaml


def parse_config():
    """ Returns a dictionary of config variables."""

    cfg = {}
    if 'AUTH_TOKEN' in os.environ:
        cfg['auth_token'] = os.environ.get('AUTH_TOKEN')
    else:
        print("The environmnet variable AUTH_TOKEN must be configured.")

    if 'CI_JOB_ID' in os.environ:
        cfg['emulation_name'] = os.environ.get('CI_JOB_ID')
    else:
        timestamp = str(time.time())
        print("CI_JOB_ID not found, defaulting to epoch timestamp {}".format(timestamp))
        cfg['emulation_name'] = timestamp

    if 'API_URL' in os.environ:
        cfg['api_url'] = os.environ.get('API_URL')
    else:
        cfg['api_url'] = 'https://api.tesuto.com/v1'

    if 'TIMEOUT' in os.environ:
        cfg['timeout'] = int(os.environ.get('TIMEOUT'))
    else:
        cfg['timeout'] = 900

    if 'CHECK_INTERVAL' in os.environ:
        cfg['check_interval'] = int(os.environ.get('CHECK_INTERVAL'))
    else:
        cfg['check_interval'] = 10

    if 'DELETE_EMULATION' in os.environ:
        cfg['delete_emulation'] = True
    else:
        cfg['delete_emulation'] = False

    # Each device in this validation must be confgiured in devices.yaml
    with open("devices.yaml", 'r') as stream:
        try:
            cfg['devices'] = yaml.load(stream)
        except Exception as e:
            print(e)
            sys.exit(1)

    # Each topology in this validation must be confgiured in topologies.yaml
    with open("topologies.yaml", 'r') as stream:
        try:
            cfg['topologies'] = yaml.load(stream)
        except Exception as e:
            print(e)
            sys.exit(1)

    # Each validator in this validation must be confgiured in validators.yaml
    with open('validators.yaml', 'r') as stream:
        try:
            cfg['validators'] = yaml.load(stream)
        except Exception as e:
            print(e)
            sys.exit(1)

    return cfg


def build_header(cfg):
    """ These headers will passed with all API requests. AUTH_TOKEN must be present in env."""

    return {
        'Authorization': 'Bearer {}'.format(cfg['auth_token']),
        'Content-Type': 'application/json',
        'Cache-Control': 'no-cache'
    }


def create_emulation(cfg):
    """ A new emulation is created with this CI JOB ID for each CI run."""

    url = '{}/emulations'.format(cfg['api_url'])
    headers = build_header(cfg)
    data = {'name': cfg['emulation_name']}
    resp = requests.request('POST', url, data=json.dumps(data), headers=headers)
    if resp.status_code != 200:
        print("Error creating emulation.")
        print(resp.text)
        sys.exit(1)
    print("Created emulation {} with ID {}".format(resp.json()['name'],
                                                   resp.json()['id']))
    return resp.json()['id']


def create_devices(cfg):
    """ Create devices specified in devices.yaml."""

    url = '{}/emulations/{}/devices'.format(cfg['api_url'], str(cfg['emulation_id']))
    headers = build_header(cfg)
    devices = []
    for device in cfg['devices']:
        data = {'name': device['name'],
                'version_id': str(device['version']),
                'model_id': str(device['model']),
                'interfaces': device['interfaces']}
        resp = requests.request('POST', url, data=json.dumps(data), headers=headers)
        if resp.status_code != 200:
            print("Error creating device")
            print("Device JSON: {}".format(json.dumps(data)))
            print(resp.text)
            sys.exit(1)
        print("Created device {} with ID {}".format(resp.json()['name'],
                                                    resp.json()['id']))
        devices.append(resp.json())

        # Upload config file for device
        config_url = "{}/emulations/{}/devices/{}/configs?api_token={}".format(
            cfg['api_url'], str(cfg['emulation_id']), str(resp.json()['id']), cfg['auth_token'])
        fin = open(device['config'], 'rb')
        files = {'file': fin}
        try:
            config_resp = requests.request('POST', config_url, files=files)
            if config_resp.status_code != 200:
                print("Error uploading configuration file.")
                print(config_resp.text)
                sys.exit(1)
            print("Uploaded configuration file {} on {}".format(device['config'],
                                                                device['name']))
        finally:
            fin.close()
    return


def create_topologies(cfg):
    """ Create topologies specified in topologies.yaml."""
    url = '{}/emulations/{}/topologies'.format(cfg['api_url'], str(cfg['emulation_id']))
    headers = build_header(cfg)
    topologies = []
    for topology in cfg['topologies']:
        data = {'data': [{
            'device': topology['device'],
            'interface': topology['interface'],
            'neighbor': topology['neighbor'],
            'neighbor_interface': topology['neighbor_interface']}]}
        resp = requests.request('POST', url, data=json.dumps(data), headers=headers)
        if resp.status_code != 200:
            print("Error creating topology")
            print("Topology JSON: {}".format(json.dumps(data)))
            print(resp.text)
            sys.exit(1)
        print("Created topology {}:{}->{}:{}".format(topology['device'],
                                                     topology['interface'],
                                                     topology['neighbor'],
                                                     topology['neighbor_interface']))
        topologies.append(resp.json())
    return


def create_validators(cfg):
    """ Add validators specified in validators.yaml. """
    url = '{}/emulations/{}/validators'.format(cfg['api_url'], str(cfg['emulation_id']))
    headers = build_header(cfg)
    validators = []
    for validator in cfg['validators']:
        data = {'script_name': validator['script_name'],
                'comment': validator['comment'],
                'parse_params': yaml.dump(validator['parse_params'], explicit_start=True,
                                          default_flow_style=False),
                'state_params': yaml.dump(validator['state_params'], explicit_start=True,
                                          default_flow_style=False)}
        resp = requests.request('POST', url, data=json.dumps(data), headers=headers)
        if resp.status_code != 200:
            print("POST JSON:")
            print(json.dumps(data, sort_keys=True, indent=2, separators=(',', ': ')))
            print("POST RESPONSE: ")
            print(resp.text)
            sys.exit(1)
        print("Created validator {} with ID {}".format(data['comment'], resp.json()['id']))
        validators.append(resp.json())
    return


def create_job(cfg):
    """ Create a job to be run now for this emulation. """
    url = '{}/emulations/jobs'.format(cfg['api_url'])
    headers = build_header(cfg)
    data = {'from_emulation': str(cfg['emulation_id'])}
    resp = requests.request('POST', url, data=json.dumps(data), headers=headers)
    if resp.status_code != 200:
        print("Error creating job")
        print("Job JSON: {}".format(json.dumps(data)))
        print(resp.text)
        sys.exit(1)
    print("Created job to run now with ID {}".format(resp.json()['id']))

    return resp.json()['id']


def watch_job(cfg):
    """ Check the stastus of the running job until completed or timeout reached. """
    current_time = int(time.time())
    to_time = current_time + cfg['timeout']
    url = '{}/emulations/jobs/{}'.format(cfg['api_url'], cfg['job_id'])
    headers = build_header(cfg)

    # Add an initial wait for status check to give job time to start
    time.sleep(int(cfg['check_interval']))

    last_status = None
    while current_time <= to_time:
        resp = requests.request('GET', url, headers=headers)
        if resp.status_code != 200:
            print("Error retrieving job.")
            print(resp.text)
        else:
            status = resp.json()['status']
            if status == 'scheduled':
                if status != last_status:
                    print("Job has not started")
            elif status in ['running', 'interactive', 'configuring', 'validating', 'initializing']:
                if status != last_status:
                    print("Job is currently running, current status: {}".format(status))
            elif status in ['cancelled', 'aborted', 'abort', 'terminated']:
                print("Job exited abnormally")
                print(resp.text)
                sys.exit(1)
            elif status == 'completed':
                print("Job completed sucessfully")
                return
            last_status = status

        # Wait for check_interval and try again
        time.sleep(int(cfg['check_interval']))
        current_time = int(time.time())

    # We passed the timeout value, exit with error
    print("Timeout exceeded, quitting")
    sys.exit(1)


def check_validations(cfg):
    """ Perform validations specified in validators.yaml. """
    url = '{}/emulations/jobs/{}/validations'.format(cfg['api_url'], cfg['job_id'])
    headers = build_header(cfg)
    resp = requests.request('GET', url, headers=headers)
    if resp.status_code != 200:
        print("Error retrieving job validation status")
        print(resp.text)
        sys.exit(1)

    fail_flag = False
    for validation in resp.json()['data']:
        print("Device {}, Validator {}, Status: {}".format(validation['device_name'],
                                                           validation['script_name'],
                                                           validation['status']))
        if validation['status'] != 'passed':
            fail_flag = True
            print("Validation failure result:")
            result = json.loads(validation['result'])
            print(json.dumps(result, sort_keys=True, indent=2, separators=(',', ': ')))

    if fail_flag is True:
        print("One or more validators failed")
        sys.exit(1)
    else:
        print("All validators passed successfully")

    return


def do_cleanup(cfg):
    """ Perform any post validation cleanup operations. """
    if cfg['delete_emulation'] is True:
        url = '{}/emulations/{}'.format(cfg['api_url'], cfg['emulation_id'])
        headers = build_header(cfg)
        resp = requests.request('DELETE', url, headers=headers)
        if resp.status_code != 200:
            print("Error deleting emulation")
            print(resp.text)
            sys.exit(1)
        print("Deleted emulation with ID {}".format(cfg['emulation_id']))
    return


if __name__ == '__main__':
    """ Run Tesuto emulation validation. """
    print('Tesuto Network Validation CI')
    cfg = parse_config()
    cfg['emulation_id'] = create_emulation(cfg)
    create_devices(cfg)
    create_topologies(cfg)
    create_validators(cfg)
    cfg['job_id'] = create_job(cfg)
    watch_job(cfg)
    check_validations(cfg)
    do_cleanup(cfg)
