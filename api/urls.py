from django.urls import path

# import views  # ModuleNotFoundError: No module named 'views'
# from api import views  # absolute imports
# import api.views as views # absolute imports
# from api.views import CategorieListView  # absolute imports
from . import views  # relative imports
# from .views import CategorieListView  # relative imports
# import .views  # err: Relative imports cannot be used with "import .a" form; use "from . import a"

app_name = 'api'

'''
base_url: api/
'''

urlpatterns = [
    path('login/', views.UserLoginView.as_view()),
    path('user/<int:pk>/', views.UserRetrieveView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('users/medecins/', views.MedecinsListView.as_view()),
    path('messages/', views.MessageListView.as_view()),
    path('send-message/', views.MessagesApiView.as_view()),
]
