from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user-signup/', views.signup, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.user_logout, name="logout"),
    path('show-journal/<int:pk>/', views.show_journal, name="showjournal"),
    path('delete/<int:pk>/', views.journal_delete, name="delete"),
    path('update/<int:pk>/', views.journal_update, name="update"),
    path('extra/', views.extra, name="extra"),
]
