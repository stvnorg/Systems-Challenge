#!/usr/bin/python

import os
from datetime import datetime, timedelta


def getHostname():
    hostname = os.popen('hostname').readlines()[0].strip('\n')
    return hostname


def getUptime():

	# The reason for not using 'uptime -p' command is because \
	# sometimes the result differ compare to the exact value as checked with 'docker ps'
	# especially after the container stopped for a while before it started

    process = os.popen('stat /proc/1/status')

    # extract /proc/1/status line 4 to get the container first access time after its start
    uptimeLine = process.readlines()[4]

    # Split the lines to extract the time
    uptimeLine = uptimeLine.strip('\n').split()

    # Date and time of the container uptime is on array [1] and [2], array[3] is for timezone UTC
    uptimeDate = uptimeLine[1]
    uptimeTime = uptimeLine[2]

    # Convert uptimeDate and uptimeTime to uptimeValue datetime python class
    uptimeDate = map(int, uptimeDate.split('-'))
    uptimeTime = map(int,uptimeTime[:8].split(':'))
    uptimeValue = eval('datetime'+str(tuple(uptimeDate + uptimeTime)))

    # To get the final uptime, substract datetime.now() with uptimeValue
    uptimeResult = datetime.now() - uptimeValue

    # Finally return the value in format 'up ..days ..hours ..minutes'
    if uptimeResult.seconds < 60: return "up less than 1 minute"
    return "up {} days, {} hours, {} minutes".format(uptimeResult.days, uptimeResult.seconds//3600, (uptimeResult.seconds//60)%60)


def getStatus(command):
	
	status = os.popen(command)
	status = [s.strip('\n') for s in status.readlines()]

	return "\n".join([""] + status)

if __name__ == '__main__':
	print getStatus("uname -r")
	print getStatus("df -h")
