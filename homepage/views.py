from django.shortcuts import render, HttpResponseRedirect, reverse

from homepage.models import Recipe
from homepage.models import Author
from homepage.forms import AddRecipe, AddAuthor


def index(request):
    my_recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": my_recipes})


def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_detail.html", {"recipe": my_recipe})

def author_detail(request, author_id):
    my_author = Author.objects.filter(id=author_id).first()
    return render(request, "author_detail.html", {"author": my_author})

def recipe_form_view(request):
    if request.method == "POST":
        form = AddRecipe(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data.get('title'),
                author=data.get('author'),
                description=data.get('description'),
                time_required=data.get('time_required'),
                instructions=data.get('instrustions'),
            )
            return HttpResponseRedirect(reverse("homepage"))
    
    form = AddRecipe()
    return render(request, "generic_form.html", {"form": form})

def author_form_view(request):
    if request.method == "POST":
        form = AddAuthor(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    
    form = AddAuthor()
    return render(request, "generic_form.html", {"form": form})