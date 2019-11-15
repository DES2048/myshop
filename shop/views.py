from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Category


class ProductList(ListView):
    queryset = Product.objects.filter(available=True)
    
    context_object_name = 'products'

    def get_queryset(self):

        qs = super().get_queryset()

        if 'category_slug' in self.kwargs:
            category = get_object_or_404(Category,
                                         slug=self.kwargs.get('category_slug'))

            qs = qs.filter(category=category)

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        ctx["categories"] = Category.objects.all()

        return ctx


class ProductDetail(DetailView):
    queryset = Product.objects.filter(available=True)
    query_pk_and_slug = True