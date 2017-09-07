# Systems Engineering Challenge

Welcome!

For this code challenge we would like to see you create infrastructure as code for 2 different tasks.


## Status Endpoint

Setup a Docker Container with a `/status` HTTP endpoint on port 8080, which should return actual system info, including the following:

- Uptime;
- Free/used memory;
- Free/used disk space;
- Kernel version;
- Last 10 syslog messages;
- Established network connections;

You can use any language you want for this task.


## MongoDB Installation with Replication

Setup a MongoDB cluster consisting of 3 shards, each shard must be a replica set of 1 primary and 2 secondaries, plus `mongos` and config server(s).

The script should be able to provision a replica set with dynamic ips.


## How to deliver your results

Fork this repo and once you're done send us a pull request. You can use any configuration management tool you wish.
