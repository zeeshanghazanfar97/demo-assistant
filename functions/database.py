import json
import random

# # Load the healthcare data
# def load_healthcare_data():
#     try:
#         with open("healthcare_data.json") as file:
#             return json.load(file)
#     except Exception as e:
#         print(e)
#         return []

# healthcare_data = load_healthcare_data()
# print("Loaded healthcare data:", healthcare_data)

# # Get a random healthcare message pair
# def get_random_healthcare_message():
#     return random.choice(healthcare_data)
# Load the healthcare data
def load_healthcare_data():
    try:
        with open("healthcare_data.json") as file:
            data = json.load(file)
            return data.get("conversations", [])  # Access the "conversations" key
    except Exception as e:
        print(e)
        return []

healthcare_data = load_healthcare_data()
print("Loaded healthcare data:", healthcare_data)

# Get a random healthcare message pair
def get_random_healthcare_message():
    return random.choice(healthcare_data)

#Get resent messages

def get_recent_messages():
    #define file name and learn instructions
    file_name = "stored_data.json"
    learn_instruction = {
     "role": "system",
     # "content" : "You are interviewing the user for a job as a retail assistant. Ask short questions relevant to a junior position.Your name is Susan. Keep your answers to under 30 words."
     "content": "You are a healthcare assistant designed to provide medical information and assistance. Respond to user queries related to general health, symptoms, and medical advice. Your name is Rachel.Keep your answers under 40 words."

    }

  #Initialise messages
    messages =[]


# Add a random element
    x = random.uniform(0,1)
    if x > 0.5 :
         learn_instruction["content"] =  learn_instruction["content"] + " Your response would include some dry humour"
    else: 
          learn_instruction["content"] =  learn_instruction["content"] + " Your response would include a rather challenging question"

 # Add a random element from healthcare_data
    x = random.uniform(0, 1)
    if x > 0.8:  # Adjust this threshold as you like
        random_message_pair = get_random_healthcare_message()
        messages.append({"role": "user", "content": random_message_pair["user"]})
        messages.append({"role": "assistant", "content": random_message_pair["assistant"]})
    

#Append instruction to message
    messages.append(learn_instruction)


    # Get last messages
    try:
         with open(file_name) as user_file:
              data= json.load(user_file)

              #Append las 5 items of data
              if data:
                   if len(data) < 5 :
                        for item in data:
                         messages.append(item)


              else:
                    for item in data[-5:]:
                         messages.append(item)
         
    except Exception as e:
         print(e)
         pass

#Return Messages

    return messages

 


#Store messages
def store_messages(request_message, response_message):
     
     #define the file name
     file_name = "stored_data.json"

     #Get recent messages
     messages = get_recent_messages()[1:]

     #Add messages to data
     user_message = {"role":"user", "content":request_message}
     assistant_message = {"role":"assistant", "content":response_message}
     messages.append(user_message)
     messages.append(assistant_message)

     #Save the updated file
     with open(file_name, "w") as f:
          json.dump(messages,f)

    #reset our messages
def reset_messages():
     
     #Overwrite current file with nothing
     open("stored_data.json", "w")
