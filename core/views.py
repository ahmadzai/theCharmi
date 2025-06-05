from django.shortcuts import render, get_object_or_404
from .models import HomeContent, Slider


def home(request):
    home_content = HomeContent.objects.all() # load all home contents,
    # we will add a flag to identify some contents as inactive in the model
    sliders = Slider.objects.all()

    if not home_content.exists():
        context = {
            'home_content': [],
            'sliders': sliders,
            'message': 'No home content available at the moment.'
        }
    else:
        context = {
            'home_content': home_content,
            'sliders': sliders
        }

    return render(request, 'core/home.html', context)
