from django.shortcuts import render


def index(request):
    return render(request, 'dict_app/index.html')


def words_list(request):
    return render(request, 'dict_app/list.html')


def add_word(request):
    return render(request, 'dict_app/add.html')
