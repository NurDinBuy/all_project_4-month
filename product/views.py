from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Foods, Categories, Pricing
from .forms import RegistrationForm


def homepage(request):
    products = Foods.objects.all()  # list
    context = {"all_food": products}
    return render(request, "product/product_list.html", context)


def Category(request):
    categories = Categories.objects.all()
    context = {"categories": categories}
    return render(request, "product/categories.html", context)


def categories_info(request, id):
    category = Categories.objects.get(id=id)
    context = {"category": category}
    return render(request, "product/category_info.html", context)


def Buy(request):
    return render(request, "product/index.html")


def register(request):
    if request.method == "POST":
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'product/register_done.html', {'new_user': new_user})
    else:
        user_form = RegistrationForm()
    return render(request, 'product/register.html', {'user_form': user_form})



class PricingListView(ListView):
    model = Pricing 
    template_name = "product/index.html"


class PricingDetailView(DetailView):
    model = Pricing
    template_name = "product/prising.html"