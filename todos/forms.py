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

class UserProfileForm(forms.ModelForm):
    class meta:
        model = UserProfile

    def clean_avatar(self):
        picture = self.cleaned_data['picture']

        try:
            w, h = get_image_dimensions(picture)

            #validate the get_image_dimensions
            max_width = max_height = 100

            if w > max_width or h>max_height:
                raise forms.ValidationError('Please user an image that is''%s x %s pixels or smaller.' % (max_width,max_height))

            main, sub = picture.content_type.split('/')
            if not (main =='image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError('Pleae user a jpeg,gif,or png image.')


