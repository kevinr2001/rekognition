from pprint import pprint

import boto3

s3 = boto3.resource('s3')

print(s3.buckets.all())

for bucket in s3.buckets.all():
    print(bucket)

print("Done.")

ec2 = boto3.resource('ec2')

print("\nEC2 Instances")
for ins in ec2.instances.all():
    pprint(ins)

print("\nEC2 Instances (id, state)")
for ins in ec2.instances.all():
    print(ins.id, ins.state)