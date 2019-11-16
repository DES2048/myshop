from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView
from .cart import Cart
from .forms import CartAddItemForm
from shop.models import Product


@require_POST
def cart_add_item(request, product_id):

    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)

    add_item_form =  CartAddItemForm(request.POST)

    if add_item_form.is_valid():
        
        form_data = add_item_form.cleaned_data

        cart.add(product, form_data['quantity'], form_data['update_qty'])

        return redirect('cart:cart_detail')


def cart_remove_item(request, product_id):
    
    cart = Cart(request)
    product = get_object_or_404(Product, pk=product_id)    

    cart.remove(product)

    return redirect('cart:cart_detail')


class CartDetailView(TemplateView):
    template_name = 'cart/cart_detail.html'

    def get_context_data(self, **kwargs):

        ctx = super().get_context_data(**kwargs)

        cart = Cart(self.request)

        ctx['cart'] = cart

        return ctx
