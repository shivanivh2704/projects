from tkinter import *

def chatbot_response(user_input):
    responses = {
        "hi": "Hello! Thanks for visiting our book shop page. How can I assist you today?",
        "hello": "Hi there! Thanks for visiting our book shop page. What can I do for you?",
        "how are you?": "I'm fine, thank you! How about you?",
        "what is your name?": "I'm a bookish chatbot created by Shivani!",
        "bye": "Goodbye! Have a great day!",
        "what genres of book you have": " fiction, non-fiction, self-help, psychology, romance, comics, philosophy, and more.",
        "tell me today's book recommendations": "'Sunrise Song,' 'Ponniyin Selvan,' and 'Percy Jackson.'",
        "tell me a joke": "Your love life.",
        "thanks": "My pleasure :)",
        "default": "I'm sorry, I don't understand that."
    }
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

wind = Tk()
wind.title('ChatBot')
wind.geometry('800x700')
wind.configure(bg='#0084ff')
xi = 0
yi = 0

def clear_message():
    global yi
    yi -= yi
    for widget in chat_bg.winfo_children():
        widget.destroy()
    yi -= 50

def send_message():
    global yi
    u = user_entry.get()
    user = Label(chat_bg, height=1, width=90, bg='#a6a6a6', fg='black', text=u + ' <You ', font=12, anchor='e')
    user.place(x=xi, y=yi)

    response = chatbot_response(u)
    bot = Label(chat_bg, height=1, width=90, bg='white', fg='black', text=f' Bot> {response}', font=12, anchor='w')
    bot.place(x=xi, y=yi + 25)

    yi += 50
    user_entry.delete(0, 'end')

hcb_text = Label(height=2, width=20, bg='#0084ff', text='HEX ChatBot', font=('Impact', 24), fg='white')
hcb_text.place(x=250, y=5)
chat_bg = Frame(height=520, width=780, bg='#f5f5f5')
chat_bg.place(x=10, y=80)
entry_bg = Frame(height=60, width=650, bg='white')
entry_bg.place(x=10, y=620)
sendbtn_bg = Frame(height=60, width=120, bg='white')
sendbtn_bg.place(x=670, y=620)

def on_enter(e):
    user_entry.delete(0, 'end')
    user_entry.config(fg='black')

def on_leave(e):
    n = user_entry.get()
    user_entry.config(fg='#5c5a5a')
    if n == '' or n == ' ':
        user_entry.insert(0, 'Enter message...')
        user_entry.config(fg='#5c5a5a')

user_entry = Entry(entry_bg, width=40, bg='white', font=('Helvetica', 20), relief=FLAT, border=0)
user_entry.place(x=10, y=13)
user_entry.insert(0, 'Enter message...')
user_entry.config(fg='#5c5a5a')
user_entry.bind("<FocusIn>", on_enter)
user_entry.bind("<FocusOut>", on_leave)

send_button = Button(sendbtn_bg, height=1, width=4, bg='#0084ff', text='➤', font=('Helvetica', 20),
                     activeforeground='white', fg='white', relief=FLAT, border=0,
                     activebackground='#0084ff', command=send_message)
send_button.place(x=5, y=4)

wind.mainloop()
