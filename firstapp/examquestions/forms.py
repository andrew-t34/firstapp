# from django import forms
#
#
# class AnswerForm(forms.Form):
#     def __init__(self, setanswers = None, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.answers = setanswers
#         self.generate_answers(self.answers)
#
#     def generate_answers(self, answers):
#         for answer in answers:
#             answe = forms.BooleanField(label = answer.text)
#             print(answe.text)
#         return answer
