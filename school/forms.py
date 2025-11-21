from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class CustomUserCreationForm(UserCreationForm):
    """A UserCreationForm that uses the project's `AUTH_USER_MODEL`.

    This avoids problems where the default form might reference
    `auth.User` directly when the user model has been swapped.
    """

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields
