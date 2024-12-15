import requests

def chat_with_huggingface(prompt):
    api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
    headers = {"Authorization": f"Bearer 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"}
    payload = {"inputs": prompt}
    
    response = requests.post(api_url, headers=headers, json=payload)
    
    # Check if the response status code is 200
    if response.status_code == 200:
        # The response is a list, so we need to access the first element
        response_data = response.json()
        return response_data[0].get("generated_text", "Sorry, I couldn't process that.")
    else:
        return f"Error: {response.status_code}, {response.text}"

if __name__ == "__main__":
    print("Chatbot: Hi there! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chat_with_huggingface(user_input)
        print("Chatbot:", response)



# import requests
# import time

# def chat_with_huggingface(prompt):
#     api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
#     headers = {"Authorization": f"Bearer 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"}
#     payload = {"inputs": prompt}
    
#     # Measure the time before making the request
#     start_time = time.time()
    
#     try:
#         response = requests.post(api_url, headers=headers, json=payload, timeout=5)  # added timeout
#         response.raise_for_status()  # Check if request was successful
#         response_data = response.json()

#         # Calculate how long the request took and print the time taken
#         elapsed_time = time.time() - start_time
#         print(f"API call took {elapsed_time:.2f} seconds.")
        
#         # Extract the generated text
#         return response_data[0].get("generated_text", "Sorry, I couldn't process that.")
    
#     except requests.exceptions.RequestException as e:
#         return f"Error: {str(e)}"

# if __name__ == "__main__":
#     print("Chatbot: Hi there! Type 'exit' to quit.")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "exit":
#             print("Chatbot: Goodbye!")
#             break
#         response = chat_with_huggingface(user_input)
#         print("Chatbot:", response)






# import requests

# def chat_with_huggingface(prompt):
#     api_url = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
#     headers = {"Authorization": "Bearer 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"}
#     payload = {"inputs": prompt}
    
#     # Make the API request and get the response
#     response = requests.post(api_url, headers=headers, json=payload)
    
#     # If the request is successful, return the generated text
#     if response.status_code == 200:
#         response_data = response.json()  # Get the response as JSON
#         return response_data[0]["generated_text"]  # Extract the generated text
#     else:
#         return "Sorry, I couldn't process that."

# if __name__ == "__main__":
#     print("Chatbot: Hi there! Type 'exit' to quit.")
#     while True:
#         user_input = input("You: ")  # Get user input
#         if user_input.lower() == "exit":  # Exit if user types 'exit'
#             print("Chatbot: Goodbye!")
#             break
#         response = chat_with_huggingface(user_input)  # Get the chatbot's response
#         print("Chatbot:", response)  # Print the response
