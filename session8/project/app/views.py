from django.shortcuts import render, redirect
from .models import POST
# from django.views.generic import ListView, DetailView, CreateView
# from .forms import PostForm

# class HomeView(ListView):
#     model = POST
#     template_name = 'home.html'
#     ordering = ['-post_date']

# class DetailView(DetailView):
#     model = POST
#     template_name = 'detail.html'

# class NewView(CreateView):
#     model = POST
#     form_class = PostForm
#     template_name = 'new.html'
#     fields = '__all__'


def home(request):
    posts = POST.objects.all()

    return render(request, 'home.html', {'posts': posts})

def new(request):
    if request.method == 'POST':
        new_post = POST.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'],
        )
        return redirect('detail', new_post.pk)
    return render(request, 'new.html')

def detail(request,	post_pk):
    post= POST.objects.get(pk=post_pk)
    
    return render(request,	'detail.html',	{'post':	post})

# Create your views here.
