from django.shortcuts import render


def index(request):
    return render(request, 'dict_app/index.html', context={'page': 'home'})


def words_list(request):
    return render(request, 'dict_app/list.html', context={'page': 'list'})


def add_word(request):
    return render(request, 'dict_app/add.html', context={'page': 'add'})
