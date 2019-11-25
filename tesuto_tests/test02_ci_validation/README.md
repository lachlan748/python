Tesuto public CI examples

This file and repository is an example use case for using Tesuto validation and emulation for
each time a configuration file is changed. This file is designed for use with gitlab-ci but the
conventions outlined are applicable to most all CI environments with minor modifications.

REQUIRED MODULES:

    pip install requests PyYAML

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

IMPORTANT NOTES:

    The timeout default is 15 minutes. Depending on size of emulation and number of validators
    this value may need to be increased.

    For documentation regarding GitLab CI/CD Variables please see their documentation at: https://docs.gitlab.com/ee/ci/variables/.


