from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, permission_required

from . import models
from .forms import SignUpForm
from .models import FoodName
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


@login_required()
def foods(request):
    paginator = Paginator(FoodName.objects.all().order_by('id'), 6)
    page_number = request.GET.get('page')
    paged_foods = paginator.get_page(page_number)
    print(FoodName.food_consistence)
    context = {
        'foods': paged_foods,
    }
    return render(request, 'foods.html', context=context)


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('index'))
    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', context={'form': form})


@permission_required('application.can_see')
@login_required()
def contacts(request):
    return render(request, 'contacts.html')

