import random
from tkinter import *

##Main Window
window = Tk();
window.title("Gues the Number Between 0 and 10")
window.configure(background="blue")

##click Function
def click():
    entered_text = inputNumber.get()
    intAnswer = int(entered_text)
    output.delete(0.0, END)

    ##Setting the random number
    randomNum = random.randint(0, 10)

    if(intAnswer > 20) or (intAnswer < 0):
        answer = "Number is out of range!"
        output.insert(END, answer)

    else:
        if (intAnswer == randomNum):
            answer = "You got it right!!"

        else:
            answer = "Better luck next time! The number was " + str(randomNum) + ". You entered " + str(intAnswer)

        output.insert(END, answer)

#Getting the input for the user

Label(window, text="Guess the Number between 0 and 20: ",bg="blue", font="none 12 bold") .grid(row=0, column=0, sticky=W)
inputNumber = Entry(window, width=30, bg="white")
inputNumber.grid(row=1, column=0, sticky=W)

##Setting submit button

Button(window, text="ENTER", width=6, command=click) .grid(row=2, column=0, sticky=W)

##Label

Label(window, text=" ", bg="blue", fg="white", font="none 12 bold")  .grid(row=3, column=0, sticky=W)

##OUTPUT TEXTBOX

output = Text(window, width=75, height=6, wrap=WORD, background="White") 
output.grid(row=4, column=0, columnspan=2, sticky=W)

##run the main loop
window.mainloop()


