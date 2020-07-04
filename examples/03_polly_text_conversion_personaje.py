import boto3

# Explicit Client Configuration
aws_session = boto3.Session(profile_name='club')


def get_text_to_audio(text, session, voice_id):
    polly = session.client('polly')
    result = polly.synthesize_speech(Text=text,
                                     OutputFormat='mp3',
                                     VoiceId=voice_id)

    # Save the Audio from the response
    audio = result['AudioStream'].read()
    with open("audio/hello_world_profile.mp3", "wb") as file:
        file.write(audio)


text_input = input()
get_text_to_audio(text_input, aws_session, "Penelope")
