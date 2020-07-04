import boto3

# Let's use Amazon S3
session = boto3.session.Session(profile_name='club')
s3 = session.resource('s3')

# S3 Object (bucket_name and key are identifiers)
obj = s3.Object(bucket_name='jug-peru-boto-3', key='hello_world.mp3')
print(obj.bucket_name)
print(obj.key)
print(obj.last_modified)

try:
    new_obj = s3.Object(bucket_name='jug-peru-boto-3')
    print(new_obj.bucket_name)
    print(new_obj.key)
except Exception as e:
    print('\033[1;31;40m {}  \n'.format(str(e)) )
