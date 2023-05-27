class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def check_answer(self, option, answer):
        if option.lower() == answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("It is wrong ")
        print(f"Correct answer is {answer}")
        print(f"Your Current score is : {self.score}/{self.question_number}")
        print("\n")

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        while self.still_has_question():
            current_question = self.questions_list[self.question_number].text
            current_answer = self.questions_list[self.question_number].answer
            self.question_number += 1
            option = input(f"Q.{self.question_number} {current_question} (True/False) : ")
            self.check_answer(option, current_answer)
        else:
            print("You have completed the quiz")
            print(f"Your final score is {self.score}/{self.question_number}")
