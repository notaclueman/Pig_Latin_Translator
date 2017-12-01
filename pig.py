import tkinter as tk

window = tk.Tk()

window.title("Pig Latin Translater")

window.geometry("600x600")

# Functions

def eng_pig():

    # split sentence into words

    input1 = str(entry1.get()).strip().lower()
    words = input1.split()
    new_words = []

    # loop through words and convert to pig latin
    # if the word starts with vowel, just add "yay"
    # otherwise, move the first consonant cluser to the end, and add "ay"

    for word in words:
        if word[0] in "aeiou":
            new_word = word + "yay"
            new_words.append(new_word)
        else:
            vowel_pos = 0
            for letter in word:
                if letter not in "aeiou":
                    vowel_pos = vowel_pos + 1
                else:
                    break
            cons = word[:vowel_pos]
            the_rest = word[vowel_pos:]
            new_word = the_rest + cons + "ay"
            new_words.append(new_word)
    output = " ".join(new_words)
    return output

def sentence_display():
    display = eng_pig()

    display_field = tk.Text(master=window, height=10, width=50)
    display_field.grid(column=1, row=2)

    display_field.insert(tk.END, display)

# Labels

label1 = tk.Label(text="Welcom to the Pig Latin Translater.\n  v1.2", font=("Times New Roman",15))
label1.grid(column=1, row=0)

# get sentence from user

label2 = tk.Label(text="Please enter a sentence:", font= 12)
label2.grid(column=0, row=1)

# Entry field 1

entry1 = tk.Entry()
entry1.grid(column=1, row=1)

# Translate Button

button1 = tk.Button(text="Translate", command=sentence_display)
button1.grid(column=2, row=1)

window.mainloop()