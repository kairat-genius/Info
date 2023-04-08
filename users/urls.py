from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns =[
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
]

# urlpatterns = [
#     path('', TestsHome.as_view(), name='home'),
#     path('about/', about, name='abouts'),
#     path('addpage', AddPage.as_view(), name='add_page'),
#     path('contact/', ContactFormView.as_view(), name='contact'),
#     path('login/', LoginUser.as_view(), name='login'),
#     path('logout/', logout_user, name='logout'),
#     path('register/', RegisterUser.as_view(), name='register'),
#     path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
#     path('category/<slug:cat_slug>/', TestsCategory.as_view(), name='category')
# ]