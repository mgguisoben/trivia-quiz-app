class Brain:

    def __init__(self, q_input):
        self.question_number = 0
        self.question_list = q_input
        self.score = 0

    def next_question(self):
        self.current_q = self.question_list[self.question_number]
        self.question_number += 1
        return self.current_q

    def check_answer(self, answer):
        if answer == self.current_q.answer:
            self.score += 1
            return True, self.score
        else:
            return False, self.score

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
