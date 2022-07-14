import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    random_number_1 = random.randint(1, 6)
    random_number_2 = random.randint(1, 6)
    random_number_3 = random.randint(1, 6)
    random_number_4 = random.randint(1, 6)
    random_number_5 = random.randint(1, 6)
    random_number_6 = random.randint(1, 6)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(title='Lottery Ticket', message=str(random_number_1)+" "+str(random_number_2)+" "+str(random_number_3)+" "+str(random_number_4)+" "+str(random_number_5)+" "+str(random_number_6))


    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
