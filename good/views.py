from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import Artiles
from .forms import ArtilesForm
from django.views.generic import DetailView, UpdateView, DeleteView


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'create'},
        {'title': "Регистрация", 'url_name': 'register'},
        {'title': "Войти", 'url_name': 'login'},
        {'title': "Выйти", 'url_name': 'logout'},
]
class NewDetaiView(DetailView):
    model = Artiles
    template_name = 'good/details_view.html'
    context_object_name = 'article'

class NewUpdateView(UpdateView):
    model = Artiles
    template_name = 'good/create.html'

    form_class = ArtilesForm

class NewDeleteView(DeleteView):
    model = Artiles
    success_url = '/home/'
    template_name = 'good/news_delete.html'

def pageNotFound(request, exception):
    return HttpResponseNotFound('Страница не найдена')

def main(request):
    return render(request, "good/main.html", {'menu': menu})

def about(request):
    return render(request, "good/about.html", {'menu': menu})

def test(requset):
    return render(requset, "good/test.html", {'menu': menu})

def index(reguest):
    return render(reguest, "good/home.html", {'menu': menu})

def news(request):
    news = Artiles.objects.order_by('title')
    return render(request, "good/news.html", {'menu': menu, 'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Форма была неверна заполнена'

    form = ArtilesForm()
    context = {
        'menu': menu,
        'form': form,
        'error': error,
    }

    return render(request, "good/create.html", context=context)


