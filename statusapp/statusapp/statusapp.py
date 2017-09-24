#!/usr/bin/python

# Docker Container status running on port 8080 using Python-Flask
# Steven Stevanus - stvn.org@gmail.com

import os
from flask import Flask, render_template, sessions, url_for, g
from container_status import getHostname, getUptime, getStatus

app = Flask(__name__)

@app.route('/status', methods=['GET','POST'])
def status():
	hostname = getHostname()
	uptime = getUptime()
	mem_usage = getStatus('free -h')
	disk_usage = getStatus("df -h")
	kernel_version = getStatus("uname -r")
	net_status = getStatus("netstat -tupan | sed -e '1,2p' -e '/ESTABLISHED/!d'")
	running_process = getStatus("ps -aux")
	return render_template("status.html", hostname=hostname, uptime=uptime, mem=mem_usage, disk=disk_usage, kernel=kernel_version, net=net_status, run_process=running_process)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)
