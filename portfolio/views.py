from django.shortcuts import render
from .models import Blog, Contact, Picture
from django.contrib import messages

# Create your views here.

def homeview(request):

    blogs = Blog.objects.all().order_by('-created')[:6]
    
    features = Blog.objects.all()

    picture = Picture.objects.get(pk = 1)

    if request.method == 'POST':
        name    = request.POST['name']
        email   = request.POST['email']
        message = request.POST['message']
        
        contact = Contact.objects.create(name = name, email = email, message= message)
        contact.save()
        
        messages.success(request, "Your message has been successfully sent!")

    context = {
        'blogs'  : blogs,
        'features' : features,
        'picture' : picture
    }
    return render(request, 'index.html', context)