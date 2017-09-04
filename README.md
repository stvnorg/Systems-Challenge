# Systems Engineering Challenge

Welcome!

For this code challenge we would like to see you create an infrastructure as code for 3 different tasks.

## Status Endpoint

Setup a Docker Container with an HTTP endpoint http://35.176.172.72:8080/status which should return actual system info, including the following:

- Uptime;
- Free/used memory;
- Free/used disk space;
- Kernel version;
- Last 10 syslog messages;
- Established network connections;

You can use any language you want for this task.


## HA Proxy Configuration

Install and configure HAProxy in a way that all incoming requests to port 80 containing only capital letters go to one HTTP server, but requests containing only digits go to another one. Any HTTP servers can be used (Nginx, Apache etc).

HAProxy must respond with 404 status code to all other requests.


## MongoDB Installation with Replication


## How to deliver your results

Fork this repo and once you're done send us a pull request.

