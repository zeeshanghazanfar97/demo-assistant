import openai
from decouple import config


# Retrieve environment variables

openai.organization = config("OPEN_AI_ORG")
openai.api_key = config("OPEN_AI_KEY")

#Import custom function
from functions.database import get_recent_messages

# OpenAI - Whisper
# Convert Audio to Text

def convert_audio_to_text(audio_file):
  try:
       transcript = openai.Audio.transcribe("whisper-1", audio_file)
       message_text = transcript["text"]
       return message_text
  except Exception as e:
    print(e)
    return


#Open AI - ChatGTP
# Get response to our message
def get_chat_response(message_input):
   messages = get_recent_messages()
   user_message = {"role": "user", "content": message_input}
   messages.append(user_message)
   print(messages)

   try:
       response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",
          messages= messages
       )
       #print(response)
       message_text = response["choices"][0]["message"]["content"]
       return message_text
   except Exception as e:
      print(e)
      return
   
   #Store messages