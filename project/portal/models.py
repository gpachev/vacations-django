from django.db import models
from django.contrib.auth.models import User


def yeld_year():
    """
    Helper function to get/set year for limit.
    Returns current year as int.
    """
    from datetime import datetime
    return datetime.now().year


class Limit(models.Model):
    """
    Contains personal limit for vacations in days.
    NOTE: these values are managed manually by admin.

    ::user - Employee
    ::year - For which year the limit is about
    ::initial - Initial amount fo days.
    ::days_left - Vacation left unspent for year.
    ::days_used - Used days this year.
    """
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    year = models.PositiveSmallIntegerField(default=yeld_year)
    initial = models.PositiveSmallIntegerField()
    days_left = models.PositiveSmallIntegerField()
    days_used = models.PositiveSmallIntegerField()

    def __str__(self):
        return "Limit for {0} @ {1}".format(self.user, self.year).capitalize()
    


class Absence(models.Model):
    """
    Absence model, containing absence related info.
    Vacations must be approved by admin.
    """
    VACATION = 'vacation'
    DELAY = 'delay'
    SICK = 'sick'

    TYPE_CHOICES = (
        (VACATION, 'Vacation'),
        (DELAY, 'Delay'),
        (SICK, 'Sick')
    )

    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    type_miss = models.CharField(max_length=10, choices=TYPE_CHOICES, default=DELAY)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{0} {1}".format(self.type_miss, self.pk).title()

    #def save(self, *args, **kwargs):
        #Should check if there is a limit for that user/year
        #Update limit on save or return error if limit reached
        #super(Absence, self).save(*args, **kwargs)