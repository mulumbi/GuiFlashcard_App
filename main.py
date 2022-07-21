"""
A GUI App made from Tkinter that helps a user learn the words in a particular language
The program shows the front of the card with the foreign word for three seconds before flipping the card
 to show the English solution
The user checks either yes or no to show if they got the word right
If the user got the word wrong they are shown the solution and the card is placed back in the deck s that
it comes back up randomly
"""
import tkinter as tk
from tkinter import *
import pandas as pd
import time as t
import random as rd
from PIL import Image

BACKGROUND_COLOR = "#B1DDC6"
YELLOW_ORANGE = "#f1a52c"

# setting up the interface
window = tk.Tk()
window.title("Flashy the Language FlashCard App")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

front_pic = PhotoImage(file="images/card_front.png")
back_pic = PhotoImage(file="images/card_back.png")
right_pic = PhotoImage(file="images/right.png")
wrong_pic = PhotoImage(file="images/wrong.png")

card = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
displayed_side = card.create_image(5, 5, anchor=NW, image=front_pic)
lang = card.create_text(400, 200, text="Language", fill="black", font=('Helvetica 24 italic'), anchor=S)
word = card.create_text(400, 250, text="Word", fill="black", font=('Helvetica 44 bold'), anchor=N)
card.grid(column=0, row=0, columnspan=2)


# reading the data from our csv file and adding it to the interface
words = pd.read_csv("data/french_words.csv")

total_words = len(words.index) - 1
correct_indexes = set()
language = words.loc[0][1]
curr_index = None

def update_values():
    # select a random pair
    card.itemconfigure(displayed_side, image=front_pic)
    random_pick = rd.randint(1, total_words)
    if random_pick in correct_indexes:
        random_pick = rd.randint(1, total_words)
    else:
        row = words.loc[random_pick]
        curr = row[0]
        translation = row[1]
        card.itemconfig(lang, text=lang)
        card.itemconfig(word, text=curr)
        window.update()
        t.sleep(3)
        card.itemconfigure(displayed_side, image=back_pic)
        card.itemconfig(word, text=translation)
        window.update()
        curr_index = random_pick



def if_correct():
    correct_indexes.add(curr_index)


start = Button(text="Start", command=update_values)
start.grid(column=0, row=4, columnspan=2)

yes = Button(text="correct", image=right_pic, highlightthickness=0, bg=BACKGROUND_COLOR,command=lambda:[if_correct(),
                                                                                                        update_values()])
no = Button(text="wrong", image=wrong_pic, highlightthickness=0, bg=BACKGROUND_COLOR,command=update_values)


yes.grid(row=3, column=1)
no.grid(row=3, column=0)
window.mainloop()
