import random
import tkinter as tk

# Main root window, min size and max size is set as well as a window title.
root = tk.Tk()
root.minsize(500,600)
root.maxsize(500,600)
root.title("Number Guessing Game")

number = int()
tries = 0
computer_number = random.randint(1,9) # Creates a random number for the computer which you have to guess
print(f'Computer number: {computer_number}') # This is for testing purposes (Can view what the machine number is to quickly go to winning frame) Delete or Comment out for no spoilers

class get_number: # Assigns the number variable the corresponding number from the pressed button

    def one(self):
        global number
        number = 1
        print(number)

    def two(self):
        global number
        number = 2
        print(number)


    def three(self):
        global number
        number = 3
        print(number)


    def four(self):
        global number
        number = 4
        print(number)


    def five(self):
        global number
        number = 5
        print(number)


    def six(self):
        global number
        number = 6
        print(number)


    def seven(self):
        global number
        number = 7
        print(number)


    def eight(self):
        global number
        number = 8
        print(number)


    def nine(self):
        global number
        number = 9
        print(number)



getting_number = get_number() # Creates an instance of the above class, called in the command parameter of each number button as getting_number.{respective fucntion}()


def win(): # Function that checks if you win or not, if you do creates a new frame with your number of tries and congratulations!

    def play_again(): # Command for play again button, basically resets everything
        global tries, computer_number
        tries = 0
        computer_number = random.randint(1, 9)

        game_text.delete('1.0', tk.END)
        top_text.delete('1.0', tk.END)
        top_text.insert(tk.END, f"{tries}")
        game_text.insert(tk.END, f"Try to guess the\nNumber :D")

        winning_frame.destroy()
        winning_text.destroy()
        again_button1.destroy()
        again_button2.destroy()

        def exit():
            root.destroy()

    if number == computer_number:

        global tries
        tries += 1
        top_text.delete('1.0', tk.END)
       
        winning_frame = tk.Frame(main_frame, bg='light blue') # Winning creates this winning frame, from each try interval a different message is outputed.
        winning_frame.pack(fill='both', expand=True)

        winning_text = tk.Text(winning_frame, state='normal', bg='light blue')
        winning_text.place(relheight=0.5, relwidth=0.5, rely=0.25, relx=0.25)

        if tries == 1:
            winning_text.insert(tk.END, f"\n\n\n\n\n\n        You WIN!!\nYou got it in {tries} try!!\n\nAmazing")
        elif tries > 1 and tries <= 10:
            winning_text.insert(tk.END, f"\n\n\n\n\n\n        You WIN!!\nYou got it in {tries} tries!!\n\nNot bad")
        else:
            winning_text.insert(tk.END, f"\n\n\n\n\n\n        You WIN!!\nBut you got it in {tries}      tries... You suck...")

        again_button1 = tk.Button(main_frame, text='Play Again ', command=lambda: play_again())
        again_button1.place(relx=0.35, rely=0.8)

        again_button2 = tk.Button(main_frame, text='Exit ', command=lambda: exit())
        again_button2.place(relx=0.55, rely=0.8)

    else: # Everytime you click a button and are wrong, this happens
        top_text.delete('1.0', tk.END)
        tries += 1
        top_text.insert(tk.END, f'{tries}')

        if number > computer_number:
            game_text.delete('1.0', tk.END)
            game_text.insert(tk.END, f"\nWrong... Guess lower")
        elif number < computer_number:
            game_text.delete('1.0', tk.END)
            game_text.insert(tk.END, f"\nWrong... Guess higher")

# Game frames 
main_frame = tk.Frame(root, bg='light blue')
main_frame.pack(fill='both', expand=True)

top_label = tk.Label(main_frame, text="Number Of\n Tries", bg='light blue')
top_label.place(relx=0.6, rely=0.05)

top_text = tk.Text(main_frame, state='normal', bg='light blue')
top_text.place(relheight=0.06, relwidth=0.06, relx=0.8, rely=0.06)
top_text.insert(tk.END, f"{tries}")

game_text = tk.Text(main_frame, bg='light blue')
game_text.place(relx=0.1, rely=0.05, relwidth=0.45, relheight=0.1)
game_text.insert(tk.END, f"Try to guess the\nNumber :D")

bottom_frame = tk.Frame(main_frame, bg='light green')
bottom_frame.place(relheight=0.8, relwidth=1, rely=0.2)

# Number buttons on bottom frame
one_button = tk.Button(bottom_frame, text='1', command=lambda: [getting_number.one(), win()])
one_button.place(relheight=0.25, relwidth=0.3, relx=0.03, rely=0.1)

two_button = tk.Button(bottom_frame, text='2', command=lambda: [getting_number.two(), win()])
two_button.place(relheight=0.25, relwidth=0.3, relx=0.35, rely=0.1)

three_button = tk.Button(bottom_frame, text='3', command=lambda: [getting_number.three(), win()])
three_button.place(relheight=0.25, relwidth=0.3, relx=0.67, rely=0.1)

four_button = tk.Button(bottom_frame, text='4', command=lambda: [getting_number.four(), win()])
four_button.place(relheight=0.25, relwidth=0.3, relx=0.03, rely=0.4)

five_button = tk.Button(bottom_frame, text='5', command=lambda: [getting_number.five(), win()])
five_button.place(relheight=0.25, relwidth=0.3, relx=0.35, rely=0.4)

six_button = tk.Button(bottom_frame, text='6', command=lambda: [getting_number.six(), win()])
six_button.place(relheight=0.25, relwidth=0.3, relx=0.67, rely=0.4)

seven_button = tk.Button(bottom_frame, text='7', command=lambda: [getting_number.seven(), win()])
seven_button.place(relheight=0.25, relwidth=0.3, relx=0.03, rely=0.7)

eight_button = tk.Button(bottom_frame, text='8', command=lambda: [getting_number.eight(), win()])
eight_button.place(relheight=0.25, relwidth=0.3, relx=0.35, rely=0.7)

nine_button = tk.Button(bottom_frame, text='9', command=lambda: [getting_number.nine(), win()])
nine_button.place(relheight=0.25, relwidth=0.3, relx=0.67, rely=0.7)

root.mainloop()
