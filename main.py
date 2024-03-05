import random
from tkinter import *
import pandas

item_index = None

try:
    open("data/words_to_learn.csv")
except FileNotFoundError:
    file_path = "data/french_words.csv"
else:
    file_path = "data/words_to_learn.csv"
finally:
    with open(file=file_path, encoding="utf-8") as data_file:
        data = pandas.read_csv(data_file)
        data_dict = data.to_dict()
        print(data_dict)


def correct_answer():
    del data_dict["French"][item_index]
    del data_dict["English"][item_index]
    with open("data/words_to_learn.csv", "w") as file:
        df = pandas.DataFrame(data_dict)
        df.to_csv(file, index=False)
    change_word()


def change_word():
    index = random.choice(list(data_dict["French"].keys()))
    card.itemconfig(image, image=FRONT)
    card.itemconfig(language, text="French")
    card.itemconfig(word, text=data_dict["French"][index])
    window.after(3000, flip, index)


def flip(index):
    global item_index
    card.itemconfig(image, image=BACK)
    card.itemconfig(language, text="English")
    card.itemconfig(word, text=data_dict["English"][index])
    item_index = index


window = Tk()

FRONT = PhotoImage(file="images/card_front.png")
BACK = PhotoImage(file="images/card_back.png")
BACKGROUND_COLOR = "#B1DDC6"

window.minsize(width=800, height=526)
window.config(pady=50, padx=70, bg=BACKGROUND_COLOR)

card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

image = card.create_image(400, 263, image=FRONT)
language = card.create_text(400, 150, text="title", font=("Comic Sans MS", 50, "italic"))
word = card.create_text(400, 300, text="word", font=("Ariel", 70, "bold"))
card.grid(row=0, column=0, columnspan=2)

correct_image = PhotoImage(file="images/right.png")
correct = Button(image=correct_image, highlightthickness=0, command=correct_answer, bd=0)
correct.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=change_word, bd=0)
wrong.grid(row=1, column=1)

change_word()

window.mainloop()
