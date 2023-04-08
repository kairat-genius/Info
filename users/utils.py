# from django.db.models import Count
from django.core.cache import cache


from good.models import Artiles

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'create'},
        {'title': "Регистрация", 'url_name': 'register'},
        {'title': "Войти", 'url_name': 'login'},
        {'title': "Выйти", 'url_name': 'logout'},

]


class DataMixin:

    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
