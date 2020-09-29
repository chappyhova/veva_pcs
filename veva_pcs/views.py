from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, QuantityForm
from django.core.mail import send_mail
from .models import Product, Basket, BasketItem
from django.views.generic import DetailView, ListView

def home(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}\n\n{2}".format(sender_name, form.cleaned_data['message'], sender_email)
            send_mail('New Enquiry', message, sender_email, ['info@vevapcs.co.uk'])

            messages.success(request, f'Your message has been sent, we aim to reply within 4 hours')
            return redirect('veva-pcs-home')
    else:
        form = ContactForm()
    
    return render(request, 'veva_pcs/home.html', {'form': form, 'products': products})

def basket(request):
    print("yaaaaaa yeeet")
    try:
        the_id = request.session['basket_id']
    except:
        the_id = None
    if the_id:
        basket = Basket.objects.get(id=the_id)
        context = {'basket': basket}
        print("yup yup")
    else:
        empty_message = "Your basket is empty, please keep shopping."
        context = {'empty': True, 'empty_message': empty_message}
    
    return render(request, 'veva_pcs/basket.html', context)

def update_basket(request, slug):
    print("i'm here")
    request.session.set_expiry(120000)
    try:
        qty = request.GET.get('qty')
        update_qty = True
    except:
        qty = None
        update_qty = False

    try:
        the_id = request.session['basket_id']
    except:
        new_basket = Basket()
        new_basket.save()
        request.session['basket_id'] = new_basket.id 
        the_id = new_basket.id 

    basket = Basket.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        pass
    except:
        pass

    basket_item, created = BasketItem.objects.get_or_create(basket=basket, product=product)
    if created:
        print("yeah")

    if update_qty and qty:
        if int(qty) == 0:
            basket_item.delete()
        else:
            basket_item.quantity = qty
            basket_item.save()  
    else:
        pass

    new_total = 0.00
    for item in basket.basketitem_set.all():
        line_total = float(item.product.price) * item.quantity
        new_total += line_total
    
    request.session['items_total'] = basket.basketitem_set.count()
    basket.total = new_total
    basket.save()
    
    return redirect('veva-pcs-basket')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'veva_pcs/product_detail.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        quantity_form = QuantityForm
        context['quantity_form'] = quantity_form
        return context


class ProductListView(ListView):
    model = Product
    template_name = 'veva_pcs/product_list.html'

def about(request):
    return render(request, 'veva_pcs/about.html')

def instagram(request):
    return redirect('https://www.instagram.com/vevapcs')

def facebook(request):
    return redirect('https://www.facebook.com/vevapcs')

def twitter(request):
    return redirect('https://www.twitter.com/vevapcs')

def products(request):
    return render(request, 'veva_pcs/products.html')