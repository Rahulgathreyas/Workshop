import cohere

# Initialize the Cohere client with your API key
co = cohere.Client('9LZHnmFcmGtH41YW4EnkBszQwkOn3xkDfjIhu73c')

# Define conversation history as a list
conversation = [
    "You are Micheal Jordan.",
    "Which shoe manufacturer are you associated with?"
]

# Function to process conversation and generate response
def chat_with_cohere(prompt):
  # Combine conversation history and prompt into a single string
  full_prompt = "\n".join(conversation + [prompt])
  response = co.generate(
      model='command-nightly',
      prompt=full_prompt,
      max_tokens=100,  # Adjust for desired response length
      temperature=0.7,  # Adjust for creativity (lower = less creative)
      k=0,
      p=0.75,
      stop_sequences=[],
      return_likelihoods='NONE'
  )
  # Access text from the first generation
  chat_response = response.generations[0].text.strip()  # Remove leading/trailing whitespace
  return chat_response

# Simulate conversation
for message in conversation:
  print(f"Human: {message}")

# Get user input
user_input = input("You: ")

# Generate response based on conversation history and user input
chat_response = chat_with_cohere(user_input)
print(f"Micheal Jordan: {chat_response}")

# Update conversation history
conversation.append(chat_response)
