from tkinter import *
from chatbot import propozitie, prelucrare_container, guess_topic, obtine_raspuns
import json


class Chatbot:
    def __init__(self, master):
        self.master = master
        master.title("Chatbot")

        # Citim fisierul intents.json cu lista de intrebari si raspunsuri
        with open("intents.json") as file:
            self.intentii_json = json.load(file)

        # Crearea etichetelor si a casetei text
        self.label = Label(master, text="Introduceti intrebarea:")
        self.label.pack()

        self.textbox = Text(master, height=1, width=70)
        self.textbox.pack()

        self.button = Button(master, text="Trimite", command=self.send)
        self.button.pack()

        self.chatlog = Text(master, height=20, width=70)
        self.chatlog.pack()

        self.chatlog.insert(END, "Bun venit! Intrebati orice doriți.\n\n")

    # Functia de trimitere a intrebarii si obtinere a raspunsului
    def send(self):
        # Citim intrebarea din caseta de text
        intrebare = self.textbox.get("1.0", 'end-1c')
        self.textbox.delete("1.0", END)

        # Obtinem topic-ul si raspunsul utilizand functiile din chatbot.py
        intentii = guess_topic(intrebare)
        raspuns = obtine_raspuns(intentii, self.intentii_json)

        # Afisam intrebarea si raspunsul in fereastra chatului
        self.chatlog.insert(END, "Utilizator: " + intrebare + "\n")
        self.chatlog.insert(END, "Chatbot: " + raspuns + "\n\n")


# Cream fereastra principala
root = Tk()
bot = Chatbot(root)
root.mainloop()
