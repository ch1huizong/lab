# -*- coding:UTF-8 -*-

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext

from .models import Band


def homepage(request):
    """
    Shows the homepage with a welcome message that is translated in the
    user's language.
    """
    message = ugettext('Welcome to our site!')
    bands = Band.objects.all()
    return render(request, 'homepage.html', {'message': message, 'bands': bands})
      

def band_listing(request):
    """A view of all bands."""
    bands = Band.objects.all()
    return render(request, 'bands/band_listing.html', {'bands': bands})


def band_detail(request, band_id):
    pass


def band_search(request):
    pass


@login_required
def my_protected_view(request):
    """A view that can only be accessed by logged-in users"""
    return render(request, 'bands/protected.html', {'current_user': request.user})
