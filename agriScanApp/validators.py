import re
from django.core.exceptions import ValidationError


def validate_password(password):
    if not re.search(r'[0-9]', password):
        raise ValidationError("The password must contain at least one number.")

    if not re.search(r'[!@#$%^&*()_\-+=\[\]{};:\'",.<>?/\\|]', password):
        raise ValidationError("The password must contain at least one special character.")

    if len(re.findall(r'[a-zA-Z]', password)) < 4:
        raise ValidationError("The password must contain at least four alphabets.")


def validate_username_length(username):
    if len(username) < 6:
        raise ValidationError("Username must have at least 6 characters.")
