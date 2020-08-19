from django import forms
from homepage.models import Recipe, Author


class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=80)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(widget=forms.Textarea)
    time_required = forms.CharField(max_length=20)
    instructions = forms.CharField(widget=forms.Textarea)