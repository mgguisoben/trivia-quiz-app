from tkinter import *

from brain import Brain

BG_COLOR = '#DBE6D1'


class QuizInterface():

    def __init__(self, brain: Brain):
        self.brain = brain

        # Initialize root window
        self.root = Tk()
        self.root.title("Trivia Quiz")
        self.root.config(pady=50, padx=50, bg=BG_COLOR)

        # Create images
        self.right_card = PhotoImage(file="images/right.png")
        self.wrong_card = PhotoImage(file="images/wrong.png")
        self.card_img = PhotoImage(file="images/card.png")
        trivia_img = PhotoImage(file="images/trivia.png")
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        # Create scoreboard
        self.score_text = Label(text=f"Score: 0", bg=BG_COLOR, font=('Helvetica', 20, 'normal'))
        self.score_text.grid(row=0, column=1, sticky='e')

        # Create a canvas
        self.card = Canvas(width=940, height=600, bg=BG_COLOR, highlightthickness=0)
        self.card.create_image(488, 30, image=trivia_img)
        self.trivia_card = self.card.create_image(488, 330, image=self.card_img)
        self.trivia_text = self.card.create_text(488, 320, width=700, justify='center',
                                                 text="Question Text", font=('Helvetica', 35, 'italic'))
        self.card.grid(row=1, column=0, columnspan=2)

        # Create buttons
        self.true_bttn = Button(image=true_img, bg=BG_COLOR, highlightthickness=0, command=self.true_pressed)
        self.true_bttn.grid(row=2, column=0)

        self.false_bttn = Button(image=false_img, bg=BG_COLOR, highlightthickness=0, command=self.false_pressed)
        self.false_bttn.grid(row=2, column=1)

        self.get_next_question()

        self.root.mainloop()

    def get_next_question(self):
        if self.brain.still_has_questions():
            current_q = self.brain.next_question()
            self.card.itemconfig(self.trivia_text, text=current_q.text)
            self.score_text.config(text=f"Score = {self.brain.score}")
            self.card.itemconfig(self.trivia_card, image=self.card_img)
        else:
            self.card.itemconfig(self.trivia_text, text="You have reached the end of the quiz.")
            self.card.itemconfig(self.trivia_card, image=self.card_img)
            self.true_bttn.config(state="disabled")
            self.false_bttn.config(state="disabled")

    def true_pressed(self):
        is_right, self.score = self.brain.check_answer("True")
        self.feedback(is_right)

    def false_pressed(self):
        is_right, self.score = self.brain.check_answer("False")
        self.feedback(is_right)

    def feedback(self, right):
        if right:
            self.card.itemconfig(self.trivia_card, image=self.right_card)

        else:
            self.card.itemconfig(self.trivia_card, image=self.wrong_card)

        self.root.after(1000, self.get_next_question)
