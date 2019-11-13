from django.shortcuts import render

posts = [
    {
        'author': 'Sean',
        'title': 'First Post',
        'content': 'First content',
        'date_posted': 'Nov 11, 2019'
    },
    {
        'author': 'Hannah',
        'title': 'Second Post',
        'content': 'Second content',
        'date_posted': 'Nov 12, 2019'
    },

]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})


