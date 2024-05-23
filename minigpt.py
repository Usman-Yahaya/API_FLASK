import tkinter as tk
from tkinter import scrolledtext
import openai # type: ignore

# Configurez votre clé API OpenAI
openai.api_key = "VOTRE_CLE_API_OPENAI"

class ChatbotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mini Chatbot GPT-3.5")
        self.geometry("400x500")

        self.chat_history = scrolledtext.ScrolledText(self, wrap=tk.WORD)
        self.chat_history.pack(expand=True, fill=tk.BOTH)

        self.input_field = tk.Entry(self)
        self.input_field.pack(expand=True, fill=tk.X)

        self.send_button = tk.Button(self, text="Envoyer", command=self.send_message)
        self.send_button.pack()

    def send_message(self):
        user_input = self.input_field.get()
        self.input_field.delete(0, tk.END)
        self.chat_history.insert(tk.END, "Vous: " + user_input + "\n")
        response = ask_gpt3(user_input)
        self.chat_history.insert(tk.END, "Chatbot: " + response + "\n")
        self.chat_history.see(tk.END)

def ask_gpt3(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    app = ChatbotApp()
    app.mainloop()
