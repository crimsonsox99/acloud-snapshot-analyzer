# acloud-snapshot-analyzer
Demo project to manage AWS EC2 instance snapshots.


## About

This project is  demo , and uses boto3 to manage AWS EC2 instance snapshots.

## Configuring

snapshot uses the configuration file created by the AWS cli. e.g.

`aws configure --profile snapshot`

## Runing

`pipenv run "python snapshot/snapshot.py <command> <subcommand> <--project=PROJECT>"`

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*project* is optional

