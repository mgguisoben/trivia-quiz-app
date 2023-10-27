from tkinter import *


root = Tk()
root.config(pady=20, padx=20)


pad_image = PhotoImage(file="images/pad.png")
pad_image = pad_image.subsample(6, 6)
right_image = PhotoImage(file="images/right.png")
right_image = right_image.subsample(30, 30)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_image = wrong_image.subsample(30, 30)

pad = Canvas(width=600, height=600)
pad.create_image(300, 300, image=pad_image)
pad.grid(row=0, column=0, columnspan=2)

right_bttn = Button(image=right_image)
right_bttn.grid(row=1, column=0)

wrong_button = Button(image=wrong_image)
wrong_button.grid(row=1, column=1)




root.mainloop()
