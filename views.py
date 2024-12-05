from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post,Category,Aboutus,Profile
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
# static demo data
# posts=[
#         {'id':1,'title':'post 1','content':'content of post 1'},
#         {'id':2,'title':'post 2','content':'content of post 2'},
#         {'id':3,'title':'post 3','content':'content of post 3'},
#         {'id':4,'title':'post 4','content':'content of post 4'},
#     ]
from django.shortcuts import render
from .models import Category

def blog_page(request):
    categories = Category.objects.all()  # Get all categories
    blog_title = "My Blog"  # Replace with your actual blog title or variable
    return render(request, 'blog_page.html', {'categories': categories, 'blog_title': blog_title})

def index1(request):
    return HttpResponse('Hello ,you are at blog index')
def index(request):
    blog_title='Latest Posts'
    all_posts=Post.objects.all()
    paginator=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    return render(request,'index.html',{'blog_title':blog_title,'page_obj':page_obj})
def detail1(request,post_id):
    return HttpResponse(f'You are viewing post detail page at {post_id}')
def detail(request,slug):
    try:
        post=Post.objects.get(slug=slug)
        related_posts=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exists")
    return render(request,'detail.html',{'post':post,'related_posts':related_posts })
def old_url_redirect(request):
    return redirect(reverse('blog:new_url'))

def new_url_view(request):
    return HttpResponse('This is new url')

@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    return render(request, 'profile.html', {'profile': profile})
def about_view(request):
    about_content=Aboutus.objects.first().content
    return render(request, 'about.html',{'about_content':about_content})


from django.shortcuts import render
from .forms import ContactForm
from .models import ContactMessage

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # Pass only request.POST, not individual fields
        if form.is_valid():
            # Manually save form data to the database
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(name=name, email=email, message=message)

            success_message = "Your message has been sent successfully!"
            return render(request, 'contact.html', {'form': form, 'success_message': success_message})
    else:
        form = ContactForm()  # For GET request, just initialize the empty form

    return render(request, 'contact.html', {'form': form})
