from django import forms

class TaskForm(forms.ModelForm):
    title = forms.CharField()
    description = forms.CharField()
    category = forms.CharField


    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if (title and content) and (title.lower() != content.lower()):
            raise forms.ValidationError('Заголовок не должен совподать')
        else:
            return cleaned_data


    def clean_title(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")

        if title and title.lower() == 'python':
            raise forms.ValidationError('слова python в загаловке нельзя использовать')
        return title
