from django import forms
from .models import Todo
from django.forms import Textarea, CheckboxInput


class TodoForm(forms.ModelForm):
	class Meta:

		model = Todo

		fields = [
		"title",
		"content",
		]


class UpdateTodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
        	"title",
            "content",
#            "created_at",
            "completed",
        ]


        widgets = {

            "content":Textarea(),
#            "created_at": forms.CharField(),
            "completed":CheckboxInput(),
        }
