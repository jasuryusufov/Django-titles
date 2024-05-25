from django.shortcuts import render
from django.views import generic
from .models import Category, Product
from random import randint
from .forms import LoginForm, RegistrationForm


class ProductList(generic.ListView):
    model = Product
    context_object_name = 'categories'
    extra_context = {
        'title': "TOTEMBO"
    }
    template_name = 'store/product_list.html'

    def get_queryset(self):
        categories = Category.objects.filter(parent=None)
        return categories


class CategoryList(generic.ListView):
    model = Product
    context_object_name = "products"
    template_name = 'store/category_page.html'

    def get_queryset(self):
        sort_field = self.request.GET.get('sort')
        type_field = self.request.GET.get('type')
        if type_field:
            products = Product.objects.filter(category__slug=type_field)
            return products
        main_category = Category.objects.get(slug=self.kwargs['slug'])
        subcategories = main_category.subcategories.all()
        products = Product.objects.filter(category__in=subcategories)
        if sort_field:
            products = products.order_by(sort_field)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        main_category = Category.objects.get(slug=self.kwargs['slug'])
        context['category'] = main_category
        context['title'] = f"Kategoriya {main_category.title}"
        return context


class ProductDetail(generic.DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        product = Product.objects.get(slug=self.kwargs['slug'])
        context['title'] = f"Mahsulot: {product.title}"
        products = Product.objects.all()
        data = []
        for i in range(4):
            random_index = randint(0, len(products) - 1)
            p = products[random_index]
            if p not in data:
                data.append(p)
        context['products'] = data
        return context


def login_registration(request):
    context = {
        'title': "Kirish yoki Ro'yxatdan o'tish",
        'login_form': LoginForm(),
        'registration_form': RegistrationForm()
    }
    return render(request, 'store/login_registration.html', context)
