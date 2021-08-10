from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from commentapp.forms import CommentCreateForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'commentapp/create.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})