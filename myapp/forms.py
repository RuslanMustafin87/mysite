from django.forms import ModelForm
from .models import Book
from django.core.exceptions import ValidationError

# class NewBookForm(forms.Form):
#     title = forms.CharField(required=True, label='Title', initial='Title')

#     def clean_title(self):
#         data = self.cleaned_data['title']

#         if (len(data) > 6):
#             raise forms.ValidationError('Error > 6')

#         return data

class NewBookForm(ModelForm):
    def clean_title(self):
        data = self.cleaned_data['book']

        if (len(data) > 6):
            raise ValidationError('Error > 6')

        return data

    class Meta:
        model = Book
        fields = ['book',]
        labels = {'book': 'title'}