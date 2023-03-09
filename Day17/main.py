# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.follower = 0
# user_1 = User("001", 'Angela', 123)
# user_2 = User("002", 'George')
#
# print(user_1.follower)
# print(user_2.follower)
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"],question['answer']))
new_q = Question(text_input="Has the day 24 hours?", answer_input="True")

brain = QuizBrain(question_bank)
while brain.still_has_question():
    brain.next_question()

