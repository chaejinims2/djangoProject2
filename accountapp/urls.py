from django.urls import path

from accountapp.views import hello_world

app_name = 'accountapp'


class AccountCreateView:
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    path('create/',AccountCreateView.as_view(), name='create')

]