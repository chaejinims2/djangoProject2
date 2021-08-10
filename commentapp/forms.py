from django.forms import ModelForm

from commentapp.models import Comment


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']