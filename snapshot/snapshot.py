import boto3
import click 

session = boto3.Session(profile_name='sandbox')
ec2 = session.resource('ec2')

def filter_instances(project):
	instances = []
	
	if project:
		filters = [{'Name':'tag:Filter','Values':[project]}]
		instances = ec2.instances.filter(Filters=filters)
	else:
		instances = ec2.instances.all()

	return instances



@click.group()
def cli():
	"""Snapshot manages snpashots"""

	
@cli.group("volumes")
def volumes():
	"""Command for volumes"""



@volumes.command('list')
@click.option('--project',default=None,
	help="Only volumes for project (tag Filter:<name>)")
def list_volumes(project):
	"List EC2 volumes"
	
	instances = filter_instances(project)
	
	for i in instances:
		for v in i.volumes.all():
			print(", ".join((
			v.id,
			i.id,
			v.state,
			v.encrypted and "Encrypted" or "Not Encrypted"
			)))

	return



	
@cli.group("instances")
def instances():
	"""Commands for instances"""



@instances.command('list')
@click.option('--project',default=None,
	help="Only instances for project (tag Filter:<name>)")
def list_instances(project):
	"List EC2 instances"
	
	instances = filter_instances(project)
	
	for i in instances:
		tags = { t['Key']: t['Value'] for t in i.tags or [] }
		print(','.join((
			tags.get('Name', '<no filter>'),
			i.id,
			i.instance_type,
			i.placement['AvailabilityZone'],
			i.state['Name'],
			i.private_dns_name)))
	return



@instances.command('stop')
@click.option('--project', default=None,
	help='Only instances for project')
def	stop_instances(project):
	"Stop EC2 instances"
	
	instances = filter_instances(project)
	
	for i in instances:
		print("Stopping {0}...".format(i.id))
		i.stop()
		
	return


@instances.command('start')
@click.option('--project', default=None,
	help='Only instances for project')
def	start_instances(project):
	"Start EC2 instances"
	
	instances = filter_instances(project)
		
	for i in instances:
		print("Starting {0}...".format(i.id))
		i.start()
		
	return


@instances.command('snapshot')
@click.option('--project', default=None,
	help='Create snapshot of all volumes')
def	start_instances(project):
	"Create snapshots for EC2 instances"
	
	instances = filter_instances(project)
	
	for i in instances:
		for v in i.volumes.all():
			print("Creating snapshot of {0}".format(v.id))
			v.create_snapshot(Description="Created by Bortlej-acloudguru training")
			
	return


	
@cli.group("snapshots")
def snapshots():
	"""Command for snapshots"""


@snapshots.command('list')
@click.option('--project',default=None,
	help="Only snapshots for project (tag Filter:<name>)")
def list_snapshots(project):
	"List EC2 snapshots"
	
	instances = filter_instances(project)
	
	for i in instances:
		for v in i.volumes.all():
			for s in v.snapshots.all():
				print(", ".join((
				s.id,
				v.id,
				i.id,
				s.state,
				s.progress,
				s.start_time.strftime("%c")
				)))

	return



	
if __name__ == '__main__':
	cli()

	