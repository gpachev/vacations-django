from django.db import models

# Create your models here.
class MissModel(models.Model):
    VACATION = 'vacation'
    DELAY = 'delay'

    TYPE_CHOICES = (
        (VACATION, 'Vacation'),
        (DELAY, 'Delay')
    )

    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    type_miss = models.CharField(max_length=10, choices=TYPE_CHOICES, default=DELAY)
    #user - current logged user (auto)
    #approved - boolean, only admins can