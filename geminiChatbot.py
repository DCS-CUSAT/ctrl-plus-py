import google.generativeai as genai
import re

# Replace with your actual Gemini API key
genai.configure(api_key='create gemini api key and paste it here')

def clean_response(text):
    text = re.sub(r'\s+', ' ', text).strip()
    text = re.sub(r'[*_]', '', text)
    paragraphs = re.split(r'\n\n|\n(?=\d+\.)', text)
    formatted_text = "\n\n".join(p.strip() for p in paragraphs if p.strip())
    return formatted_text

def chat():
    print("Chatbot: Hello! Ask me anything 😊 (type 'exit' to quit)")
    model = genai.GenerativeModel('gemini-2.0-flash')
    chat_session = model.start_chat(history=[])

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        response = chat_session.send_message(user_input)
        reply = response.text
        cleaned_reply = clean_response(reply)
        print("Chatbot:", cleaned_reply)
        print("-" * 30)

chat()