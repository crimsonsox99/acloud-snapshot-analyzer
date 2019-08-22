from setuptools import setup

setup (
	name="snapshot-analyzer",
	version='0.1',
	author="Jeff Bortle",
	author_email="jeffrey.bortle@umassmed.edu",
	description="snaphot=analyzer is a tool to manage AWS EC2 sanshots.",
	license="GPLv3+",
	packages=['snapshot'],
	url="https://github.com/crimsonsox99/acloud-snapshot-analyzer",
	install_requires=[
		'click',
		'boto3'
	],
	entry_points='''
		[console_scripts]
		snapshot=snapshot:cli
	''',
)