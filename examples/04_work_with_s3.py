import boto3

# Let's use Amazon S3
session = boto3.session.Session(profile_name='club')
s3 = session.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

data = open('audio//hello_world.mp3', 'rb')
s3.Bucket('jug-peru-boto-3').put_object(Key='hello_world.mp3', Body=data)
