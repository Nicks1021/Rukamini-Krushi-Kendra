
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Product, Category


def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "index.html", {
        "products": products,
        "categories": categories
    })


def owner_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        return render(request, "login.html", {
            "error": "Username किंवा Password चुकीचा आहे."
        })

    return render(request, "login.html")


@login_required
def dashboard(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(request, "dashboard.html", {
        "products": products,
        "categories": categories
    })


@login_required
def add_product(request):

    if request.method == "POST":

        name = request.POST.get("name")
        category_id = request.POST.get("category")
        description = request.POST.get("description")
        price = request.POST.get("price")
        stock = request.POST.get("stock")
        image = request.FILES.get("image")

        category = Category.objects.get(id=category_id)

        Product.objects.create(
            name=name,
            category=category,
            description=description,
            price=price,
            stock=stock,
            image=image
        )

        return redirect("dashboard")

    categories = Category.objects.all()

    return render(request, "add_product.html", {
        "categories": categories
    })


@login_required
def edit_product(request, product_id):

    product = Product.objects.get(id=product_id)

    if request.method == "POST":

        product.name = request.POST.get("name")
        product.category_id = request.POST.get("category")
        product.description = request.POST.get("description")
        product.price = request.POST.get("price")
        product.stock = request.POST.get("stock")

        if request.FILES.get("image"):
            product.image = request.FILES.get("image")

        product.save()

        return redirect("dashboard")

    categories = Category.objects.all()

    return render(request, "edit_product.html", {
        "product": product,
        "categories": categories
    })


@login_required
def delete_product(request, product_id):

    product = Product.objects.get(id=product_id)

    if request.method == "POST":
        product.delete()
        return redirect("dashboard")

    return render(request, "delete_product.html", {
        "product": product
    })


@login_required
def add_category(request):

    if request.method == "POST":

        name = request.POST.get("name")

        if name:
            Category.objects.create(
                name=name
            )

        return redirect("dashboard")

    return render(request, "add_category.html")


@login_required
def owner_logout(request):
    logout(request)
    return redirect("owner_login")

