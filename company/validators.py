from django.core.exceptions import ValidationError
from datetime import date






def date_in_future_validator(date_):
    if date_ > date.today():
        # wenn das eintritt, ist das nicht legal!
        raise ValidationError("Das Datum darf nicht in der Zukunft liegen!")
    return date_
def digits_only_validators(value):
    if all(i.isdigit() for i in value):
        raise ValidationError("Der name darf nicht nur aus zahlen bestehen!")  
    return value 