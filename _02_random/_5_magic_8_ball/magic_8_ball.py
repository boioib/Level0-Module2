import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    answer = simpledialog.askstring(title='8 Ball',prompt='Ask me a question')
    # Make a variable and initialize it to a random number between 0 and 3
    random_num=random.randint(0, 3)
    # If the random number is 0
    if random_num ==0:
        messagebox.showinfo(title='Response', message='Yes')
        # tell the user "Yes"

    # If the random number is 1
    if random_num ==1:
        messagebox.showinfo(title='Response', message='No')
        # tell the user "No"

    # If the random number is 2
    if random_num ==2:
        messagebox.showinfo(title='Response', message='Maybe you should ask google')
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3
    if random_num ==3:
        messagebox.showinfo(title='Response', message='You should ask another question.')
        # write your own answer
