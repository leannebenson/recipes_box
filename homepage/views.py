from django.shortcuts import render

from homepage.models import Recipe
from homepage.models import Author

def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes})


def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_detail.html", {"recipe": my_recipe})

def author_detail(request, author_id):
    my_author = Author.objects.filter(id=author_id).first()
    return render(request, "author_detail.html", {"author": my_author})