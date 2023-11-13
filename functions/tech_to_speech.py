import requests
from decouple import config
from elevenlabs import Voice, VoiceSettings, generate


ELEVEN_LABS_API_KEY = config("ELEVEN_LABS_API_KEY")

#Eleven labs
#Convert text to speech

def convert_text_to_speech(message):
  audio = generate(
      text=message,
      voice=Voice(
          voice_id='21m00Tcm4TlvDq8ikWAM',
          settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
      )
  )
  print("Audio generated")
  return audio

  body = {
  "text": message,
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0,
    "similarity_boost": 0,
    "style": 0,
    "use_speaker_boost": "true"
  }
}

  #Define Voice
  voice_rachel ="21m00Tcm4TlvDq8ikWAM"

  #constructing header and endpoints
  print("eleven labs " + ELEVEN_LABS_API_KEY + "!")

  headers = {
    "xi-api-key": ELEVEN_LABS_API_KEY,
    "Content-Type": "application/json",
    "accept": "audio/mpeg"
  }
  endpoint = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_rachel}"

  #Send request
  try:
   response = requests.post(endpoint, json=body, headers=headers)
  except Exception as e:
   print(e)
   return
  
  #Handle Response
  if response.status_code == 200:
    return response.content
  else:
    return