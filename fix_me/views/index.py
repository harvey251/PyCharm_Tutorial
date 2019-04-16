from django.shortcuts import render


def index(request):
    # TODO: Ctrl+Alt+Backspace
    return render(request, 'todos.html')
