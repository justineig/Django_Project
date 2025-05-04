from django.shortcuts import render
from django.utils import timezone

def home(request):
    return render(request, "Home.html")


def advanced_news(request):
     news_items = [
        {
            'title': 'New Breakthrough in Renewable Energy',
            'category': 'Technology',
            'pub_date': timezone.now() - timezone.timedelta(days=1),
            'views': 1245
        },
        {
            'title': 'Global Summit on Climate Change',
            'category': 'Environment',
            'pub_date': timezone.now() - timezone.timedelta(days=2),
            'views': 892
        }
        ]
     context = {
        'news_items': news_items,
    }
     return render(request, "news_advanced.html", context)
