
from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages
from .models import *
from .forms import ContactForm, SubscribeNewsletterForm

menu = [{'title': "Močiutės užrašai", 'url_name': "blog"},
        {'title': "Produktai", 'url_name': "products"},
        {'title': "Kontaktai", 'url_name': "contacts"},
        ]

def index(request):
    context = {
        'menu': menu,
        'title': 'Močiutės kepyklėlė',
        'title2': 'Puikus skonis, pagardintas meile'
    }
    return render(request, 'mk/index.html', context=context)

def blog(request):
    blogpost = BlogPost.objects.all()
    context = {
        'menu': menu,
        'blogpost': blogpost,
        'title': 'Močiutės užrašai',
        'title2': 'Užrašai iš močiutės gyvenimo',
    }
    return render(request, 'mk/blog.html', context=context)

def blogPost(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)
    context = {
        'menu': menu,
        'blogpost': blogpost,
        'title': 'Blogo įrašas'
    }
    return render(request, 'mk/blogPost.html', context=context)

def products(request):
    category = Category.objects.all()
    context = {
        'menu': menu,
        'category': category,
        'title': 'Produktai',
        'title2': 'Gardūs naminiai kepiniai',
    }
    return render(request, 'mk/products.html', context=context)

def showProducts(request, slug):
    if(Category.objects.filter(slug=slug)):
        products = Product.objects.filter(category__slug=slug)
        category_name = Category.objects.filter(slug=slug).first()
        context = {
            'menu': menu,
            'products': products,
            'category_name': category_name,
        }
        return render(request, 'mk/showProducts.html', context=context)
    else:
        messages.warning(request, "Nėra pasirinktos kategorijos")
        return redirect('products')

def contacts(request):
    # Newsletter registration
    newsletter_form = SubscribeNewsletterForm(request.POST or None)
    if newsletter_form.is_valid():
        instance = newsletter_form.save(commit=False)
        if NewsletterUser.objects.filter(user_email = instance.user_email).exists():
            messages.error(request, 'Įvestas el. pašto adresas jau yra')
        else:
            instance.save()
            messages.success(request, 'Sėkmingai prenumeravote naujienlaiškį!')
        return redirect('contacts')
    # Send message to email form
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            EmailMessage('Contact Form Submission from {}'.format(name),
               message, 'form-response@example.com', ['gintas.strz@gmail.com'], [],
               reply_to=[email]).send()
            messages.success(request, 'Jūsų žinutė sėkmingai išsiųsta!')
            return redirect('contacts')
    else:
        contact_form = ContactForm()
    context = {
        'menu': menu,
        'newsletter_form': newsletter_form,
        'contact_form': contact_form,
        'title': 'Kontaktai',
        'title2': 'Kontaktai',
        'title3': 'Turite klausimų? Susisiekime!'
    }
    return render(request, 'mk/contacts.html', context=context)

    
