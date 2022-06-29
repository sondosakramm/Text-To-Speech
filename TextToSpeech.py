import requests
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig

subscription_key = 'YOUR KEY'
region = 'eastus'
endpoint = 'YOUR ENDPOINT'

def get_token(subscription_key):
    fetch_token_url = endpoint
    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key
    }
    response = requests.post(fetch_token_url, headers=headers)
    access_token = str(response.text)
    print(access_token)

speech_config = SpeechConfig(subscription=subscription_key,region=region)
speech_config.speech_synthesis_voice_name = "de-DE-KatjaNeural"

audio_config = AudioOutputConfig(filename="FILENAME.wav")
synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
file = open('YOUR TEXT FILE LOCATION', mode='r',encoding='utf-8')
all_of_it = file.read()
file.close()
synthesizer.speak_text_async(all_of_it)
