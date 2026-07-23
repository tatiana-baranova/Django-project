from django.shortcuts import render


def home(request):
    news = [
        {
            'title': 'News 1',
            'text': 'This is the first news item.',
            'date': '2026-01-23',
        },
        {
            'title': 'News 2',
            'text': 'This is the second news item.',
            'date': '2026-01-24',
            'author': 'Author 2',
        },
    ]
    
    data = {
        'news': news,
        'title': 'Home Page',
    }
    return render(request, 'blog/home.html', data)

def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact Page'})