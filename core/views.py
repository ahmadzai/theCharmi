from django.shortcuts import render, get_object_or_404
from .models import HomeContent, Slider


def home(request):
    home_content = get_object_or_404(HomeContent, pk=1)  # Assuming single HomeContent
    sliders = Slider.objects.all()
    return render(request, 'core/home.html', {'home_content': home_content, 'sliders': sliders})
