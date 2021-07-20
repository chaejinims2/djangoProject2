from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.fields['username'].disabled = True
