from django.shortcuts import render, redirect


def index(request):
    return render(request, 'dict_app/index.html', context={'page': 'home'})


def read_from_file():
    with open('dict_app/static/words_for_dict.txt', 'r', encoding='utf-8') as file:
        all_words = file.read().splitlines()
        words = {}
        for row in all_words:
            word1, word2 = row.split()
            words.setdefault(word1, word2)
        return words


def words_list(request):
    words = read_from_file()
    return render(request, 'dict_app/list.html', context={'page': 'list', 'content': words})


def add_to_file(w1: str, w2: str):
    with open('dict_app/static/words_for_dict.txt', 'a', encoding='utf-8') as file:
        file.write(w1 + ' ' + w2 + '\n')


def add_word(request):
    if request.method == 'GET':
        return render(request, 'dict_app/add.html', context={'page': 'add'})
    else:
        add_to_file(request.POST['word1'], request.POST['word2'])
        return redirect(index)


