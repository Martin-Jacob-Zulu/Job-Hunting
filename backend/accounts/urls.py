from django.urls import path
from .views import SignupView, account_properties_view, account_update_view


urlpatterns = [
    path('myaccount', account_properties_view),
    path('myaccount/update', account_update_view),
    path('signup', SignupView.as_view()),
]