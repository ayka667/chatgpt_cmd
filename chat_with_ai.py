import os
import json
import openai
from datetime import datetime

def load_api_key():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config['openai_api_key']

openai.api_key = load_api_key()

def create_history_folder():
    if not os.path.exists('historique'):
        os.makedirs('historique')

def get_filename():
    today = datetime.now().strftime("%d %m %Y")
    return f"historique/{today}.txt"

def log_conversation(conversation):
    filename = get_filename()
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(conversation + '\n')

def get_ai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content'].strip()

def chat_with_ia():
    create_history_folder()
    print("Bienvenue! Tape 'exit' pour quitter la conversation.")
    conversation_history = [{"role": "system", "content": "Tu es un assistant IA utile."}]
    
    while True:
        user_input = input("Vous: ")
        if user_input.lower() == 'exit':
            print("Fin de la conversation.")
            break

        conversation_history.append({"role": "user", "content": user_input})
        
        ia_response = get_ai_response(conversation_history)
        
        print(f"IA: {ia_response}")
        
        conversation_history.append({"role": "assistant", "content": ia_response})

        log_conversation(f"Vous: {user_input}")
        log_conversation(f"IA: {ia_response}")

if __name__ == "__main__":
    chat_with_ia()
