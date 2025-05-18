from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactInquiry
from .forms import ContactInquiryForm


def contact(request):
    return render(request, 'contact/contact.html')


def contact_submit(request):
    if request.method == 'POST':
        form = ContactInquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(
                f'<h5>'
                'Your inquiry has been submitted successfully!'
                '</h5>', status=200)
        else:
            errors = form.errors.as_json()
            return HttpResponse(f'<div class="bg-red-100 text-red-800 p-4 rounded">Error: {errors}</div>', status=400)
    return HttpResponse('<div class="bg-red-100 text-red-800 p-4 rounded">Invalid request method.</div>', status=400)
