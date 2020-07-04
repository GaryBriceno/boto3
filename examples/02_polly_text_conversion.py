import boto3

# Explicit Client Configuration
session = boto3.Session(profile_name='club')
polly = session.client('polly')

result = polly.synthesize_speech(Text='Hello World!',
                                 OutputFormat='mp3',
                                 VoiceId='Aditi')

# Save the Audio from the response
audio = result['AudioStream'].read()
with open("audio/hello_world_profile.mp3", "wb") as file:
    file.write(audio)
