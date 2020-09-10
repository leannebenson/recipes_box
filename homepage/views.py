from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from homepage.models import Recipe
from homepage.models import Author
from homepage.forms import AddRecipe, AddAuthor, LoginForm, SignupForm


def index(request):
    my_recipes = Recipe.objects.all()
    print(my_recipes)
    return render(request, "index.html", {"recipes": my_recipes})


def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_detail.html", {"recipe": my_recipe})

def author_detail(request, author_id):
    my_author = Author.objects.filter(id=author_id).first()
    return render(request, "author_detail.html", {"author": my_author})

@login_required
def recipe_form_view(request):
    if request.method == "POST":
        form = AddRecipe(request.POST)
        form.save()
        author=request.user
        return HttpResponseRedirect(reverse("homepage"))
    
    form = AddRecipe()
    return render(request, "generic_form.html", {"form": form})

@login_required
def author_form_view(request):
    if request.method == "POST":
        form = AddAuthor(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    
    form = AddAuthor()
    return render(request, "generic_form.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data.get("username"), password=data.get("password"))
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))

    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})

def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(username=data.get("username"), password=data.get("password"))
            Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))

    form = SignupForm()
    return render(request, "generic_form.html", {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))