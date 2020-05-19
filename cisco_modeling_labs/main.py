import urllib3
from virl2_client import ClientLibrary
from pprint import pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
client = ClientLibrary("https://192.168.137.252", "admin", "cakeface99", ssl_verify=False)
client.wait_for_lld_connected()

for lab in client.all_labs():
    print("Current labs on CML include:\n")
    print(f"Lab ID {lab.id}, Title: {lab.title}\n")
    print(f"Starting lab {lab.id}")
    lab.start()
    #pprint(dir(lab))
