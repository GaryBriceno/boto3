from util.config import ACCESS_KEY_ID
from util.config import SECRET_ACCESS_KEY
from util.config import REGION_NAME

import boto3

client = boto3.client('ses',
                      aws_access_key_id=ACCESS_KEY_ID,
                      aws_secret_access_key=SECRET_ACCESS_KEY,
                      region_name=REGION_NAME)

client.send_email(
    Source="gary.briceno@gmail.com",
    Destination={
        # List of emails to send the email
        'ToAddresses': ['gary.briceno@gmail.com']
    },
    Message={
        'Subject': {
            # title of the email to send
            'Data': 'AWS SDK para Python (Boto3)',
            'Charset': 'UTF-8'
        },
        'Body': {
            'Text': {
                # body of the email
                'Data': "Esto es un ejemplo de mensaje utilizando Boto3.",
                'Charset': 'UTF-8'
            }
        }
    }
)
