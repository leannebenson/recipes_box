from django import forms
from homepage.models import Recipe, Author


class AddRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "author", "description", "time_required", "instructions"]

class AddAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "bio"]