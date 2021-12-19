from django.shortcuts import render
from cart.forms import CartAddProductForm
from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Team
from .recommender import Recommender
from django.views.generic import CreateView

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    cart_product_form = CartAddProductForm()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,'ecomerce/list.html',{'category': category,'categories': categories,'products': products,'cart_product_form': cart_product_form})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 5)
    return render(request,'ecomerce/detail.html',{
        'product': product,
        'cart_product_form': cart_product_form,
        'recommended_products': recommended_products,    
    })
def about(request):
    team = Team.objects.all()

    return render(request, 'ecomerce/about us.html',{
        'team':team,
    })

class JoinTeam(CreateView):
    model = Team
    fields = 'img','name','position','email','fb_link','twitter_link','whatsapp_link','linkedin'
    template_name = 'ecomerce/join team.html'

def app_success(request):
    return render(request, 'ecomerce/success.html')

    