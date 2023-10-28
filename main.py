from brain import Brain
from data import question_data
from question import Question
from ui import QuizInterface

question_bank = [Question(q['text'], q['answer']) for q in question_data]

brain = Brain(question_bank)

quiz_interface = QuizInterface(brain)
