import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("KHAY (AI)")
app.geometry("500x600")

img = Image.open("btn.png")

def send_message(event=None):
    user_message = entry.get().strip()

    if user_message.lower() in ["quit", "exit", "close", "stop"]:
        app.quit()

    if user_message:
        chat_history.configure(state="normal")
        chat_history.insert("end", "You: ", "user_tag")
        chat_history.insert("end", f"{user_message}\n")
        entry.delete(0, "end")
        bot_response = reply(user_message)
        chat_history.insert("end", "ChatAI: ", "bot_tag")
        chat_history.insert("end", f"{bot_response}\n\n")
        chat_history.configure(state="disabled")
        chat_history.yview("end")

def reply(message):
    responses = {
        **dict.fromkeys(["hello", "hi"], "Hi there! How can I help?"),
        **dict.fromkeys(["help", "rules"], "I can help you with that. Just ask!"),
        **dict.fromkeys(["what is your name", "who are you"], "I'm a chatbot created by KhayAI!"),
        "how are you": "I'm just a bot, but I'm doing great!",
        "bye": "Goodbye! Have a nice day.",
    }
    return responses.get(message.lower(), "Sorry, I don't understand.")

chat_history = ctk.CTkTextbox(app, height=500, width=480, wrap="word", state="disabled")
chat_history.pack(padx=10, pady=10)

chat_history.tag_config("user_tag", foreground="cyan")  
chat_history.tag_config("bot_tag", foreground="light green")

entry = ctk.CTkEntry(app, width=380, height=40,corner_radius=36, border_color="red", placeholder_text="Type a message...")
entry.pack(pady=5, padx=5, side="left")
entry.bind("<Return>", send_message)

send_button = ctk.CTkButton(app, text="Send", corner_radius=32, fg_color="transparent",
                            border_color="red", border_width=2, image=ctk.CTkImage(dark_image=img),
                            font=("Arial", 13, "bold"), command=send_message)
send_button.pack(pady=5, padx=10, side="right")

app.mainloop()
