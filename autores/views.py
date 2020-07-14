from django.shortcuts import render

from autores.models import Author


def authors(request):
    autores = Author.objects.all()
    context = {
        'autores': autores
    }
    return render(request, 'autores/listar.html', context=context)
