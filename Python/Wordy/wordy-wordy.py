######      ###   #
##### BY VAHEMA ###
######      ###  ##

import random, os, pyfiglet

banner = pyfiglet.figlet_format("WORDY WORDY")
guessed_words = 0
combo = 0
last_word = ""
true_meaning = ""
wrong_word = ""

a = input(print(banner, "PRESS ENTER TO PLAY..."))

def select_word():
    global combo, guessed_words, last_word, true_meaning, wrong_word

    with open("words.txt", "r", encoding="utf-8") as file:
        words = [line.strip() for line in file]

    while True:
        diff_word = True

        while diff_word:
            choosen_word = random.choice(words)
            word, meaning = choosen_word.split(" - ")

            if choosen_word != last_word:
                last_word = choosen_word
                diff_word = False

        os.system("clear")

        print(f"""
    ###################
    #####        ######
    ###  {word.upper()}
    #####          #### 
    ###################
    |COMBO : {combo}|
    |GUESSED WORDS : {guessed_words}|
    |{wrong_word.upper()} - {true_meaning.upper()}|
            """)

        guess = input(">>> ")

        if guess.lower() == meaning:
            guessed_words += 1
            combo += 1
            true_meaning = ""
            wrong_word = ""
        else:
            combo = 0
            wrong_word = word
            true_meaning = meaning

if __name__ == "__main__":
    select_word()
