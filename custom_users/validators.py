import re

from rest_framework import validators
from zxcvbn import zxcvbn


def validate_password(data):
    fields = ["name", "email"]
    score_fields = [data[key] for key in fields if data[key] is not None]
    results = zxcvbn(data["password"], user_inputs=score_fields)
    if results["score"] < 3:
        warning = "Password is weak."
        suggestions = results["feedback"]["suggestions"]
        raise validators.ValidationError(warning + " " + " ".join(suggestions))
