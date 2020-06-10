import re
import datetime

startTime = datetime.datetime.now()

with open('sample_log_anonymized.log', 'r') as f:
	for line in f.readlines():
		if re.search('ACLLOG-5-ACLLOG_FLOW_INTERVAL', line):
			print(line)


endTime = datetime.datetime.now()
elapsedTime = endTime - startTime
print(f"Time Elapsed: {elapsedTime}")