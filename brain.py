class Brain:

    def __init__(self, q_input):
        self.question_number = 0
        self.question_list = q_input
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        return current_q

    def check_answer(self, answer, correct):
        if answer == correct:
            self.score += 1
