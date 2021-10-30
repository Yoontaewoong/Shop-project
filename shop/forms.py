from django import forms
from .models import Question, Answer, Notice, Review


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['q_title', 'q_content']

        labels = {
            'q_title': '제목',
            'q_content': '내용',
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['a_content']
        labels = {
            'a_content': '답변내용',
        }
