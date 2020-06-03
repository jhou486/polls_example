from django.urls import path
from . import views
from django.conf.urls import url


app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
    path('polls/<int:question_id>/results', views.results, name='result'),

    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),

    path('form-test/', views.form_test, name='form-test'),
    path('person-test/', views.person_test, name='person-test'),
    path('dj/person-test/<int:pid>/', views.person_test_detail, name='person-test-id')


]

