from django import forms
from tasks.models import Category


class searchForm(forms.Form):
    search = forms.CharField(required=False,
                             max_length=100,
                             widget=forms.TextInput(attrs={
                                 'placeholder': 'Введите название',
                                 'class': 'form-control'}))

    category = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    orderings = (
        ('title', "По названию"),
        ('-title', 'По названию в обратном порядке')
    )