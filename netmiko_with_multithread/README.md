This script:

*  reads an ansible inventory file
*  connects to each device, sends a list of 'show' commands
*  collects the output and writes to a unique text file within a directory per device
