# Importing libraries
import random

# List of possible responses
responses = {
  "greeting": ["Hello!", "Hi there!", "Hi!", "Hello there!", "Hi everyone!"],
  "farewell": ["Goodbye!", "See you later!", "Have a great day!", "Goodbye for now!"],
  "affirmative": ["Yes.", "Of course!", "Definitely!", "Sure thing!", "Absolutely!"],
  "negative": ["No.", "Nope.", "No way.", "Not really.", "I don't think so."],
  "studydetails": ["The course is a 3 year course. The syllabus is as follows: 1st year: 1st sem: Maths, Physics, Chemistry, English, 2nd sem: Maths, Physics, Chemistry, English, 2nd year: 1st sem: Maths, Physics, Chemistry, English, 2nd sem: Maths, Physics, Chemistry, English, 3rd year: 1st sem: Maths, Physics, Chemistry, English, 2nd sem: Maths, Physics, Chemistry, English, "]
}

# Function to generate a response
def generate_response(prompt):
  if "hello" in prompt.lower() or "hi" in prompt.lower():
    return random.choice(responses["greeting"])
  elif "bye" in prompt.lower() or "goodbye" in prompt.lower():
    return random.choice(responses["farewell"])
  elif "course" in prompt.lower() or "syllabus" in prompt.lower():
    return random.choice(responses["studydetails"])
  elif "yes" in prompt.lower() or "yea" in prompt.lower():
    return random.choice(responses["affirmative"])
  elif "no" in prompt.lower() or "nope" in prompt.lower():
    return random.choice(responses["negative"])
  else:
    return "I'm sorry, I don't understand what you're saying."

# Main function to run the chatbot
def run_chatbot():
  print("Hi! I'm a chatbot for the college website. How can I help you today?")
  while True:
    prompt = input("You: ")
    response = generate_response(prompt)
    print("Chatbot: " + response)
    if "Bye" in prompt.lower() or "goodbye" in prompt.lower():
      break

# Running the chatbot
run_chatbot()