from django.shortcuts import render
from .models import User


def UserList(request):
    user = User.objects.using('users_db').all()
    context = {
        "users": user
    }
    return render(request, 'user/index.html', context)

