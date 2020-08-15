from django.shortcuts import render

from homepage.models import Recipe

def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes})


def recipes_detail(request, recipe_id):
    my_recipe = Recipe.object.filter(id=recipe_id).first()
    return render(request, "recipe.detail.html", {"recipe": my_recipe})