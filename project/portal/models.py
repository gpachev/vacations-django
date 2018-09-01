from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Absence(models.Model):
    """
    Absence model, containing absence related info.
    Vacations must be approved by admin.
    """
    VACATION = 'vacation'
    DELAY = 'delay'

    TYPE_CHOICES = (
        (VACATION, 'Vacation'),
        (DELAY, 'Delay')
    )

    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    type_miss = models.CharField(max_length=10, choices=TYPE_CHOICES, default=DELAY)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "Vacation {0}".format(self.pk)