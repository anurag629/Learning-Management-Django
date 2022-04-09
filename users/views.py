from pyexpat.errors import messages
from django.shortcuts import render, redirect

from users.forms import UserRegisterForm

# Create your views here.


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.changed_data.get('username')
            messages.success(
                request, f'Account created for the {username} successfully!')
            return redirect('login')

        else:
            form = UserRegisterForm()

        return render(request, 'user/register.html', {'form': form})
