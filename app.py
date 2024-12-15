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
