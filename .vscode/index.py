import google.generativeai as genai
import tkinter as tk
from tkinter import Scrollbar, Text

# Configure API Key
genai.configure(api_key="AIzaSyCDdXqzynf-zIt4cUox1pic3qHhnj3lZ-U") 

# Initialize chat model
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Function to send message and get response
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return  # Ignore empty input

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You : " + user_input + "\n", "user")
    chat_window.config(state=tk.DISABLED)

    entry.delete(0, tk.END)  # Clear input field
    root.update()

    try:
        response = chat.send_message(user_input)
        bot_reply = response.text.strip()
    except Exception as e:
        bot_reply = "Error: Could not fetch response. Check API key."

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "Chatbot : " + bot_reply + "\n", "bot")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)  # Auto-scroll to latest message

# Create UI
root = tk.Tk()
root.title("Chatbot")

# Chat window
chat_window = Text(root, wrap=tk.WORD, state=tk.DISABLED, font=("Arial", 12), bg="#f0f0f0")
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Scrollbar
scrollbar = Scrollbar(root, command=chat_window.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
chat_window.config(yscrollcommand=scrollbar.set)

# Input field
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(padx=10, pady=5, fill=tk.X)

# Send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12), bg="#4CAF50", fg="white")
send_button.pack(pady=5)

# Styling chat messages
chat_window.tag_config("user", foreground="blue")
chat_window.tag_config("bot", foreground="red")

root.mainloop()
