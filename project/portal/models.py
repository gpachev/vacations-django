from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

def yeld_year():
    """
    Helper function to get/set year for limit.
    Returns current year as int.
    """
    return datetime.now().year

def calculate_timedelta(from_date, to_date):
    """
    Helper function to calculate how many days the vacation is.
    """
    days_as_timedelta = to_date.date() - from_date.date()
    days_as_int = days_as_timedelta / timedelta(days=1) #hack in P3
    return days_as_int

def update_limiter(days, limiter):
    """
    Helper function to calculate days for Vacation and update limiter
    """
    new_days_left = limiter.days_left - days
    new_days_used = limiter.days_used + days

    limiter.days_left=new_days_left
    limiter.days_used=new_days_used
    #specify which fields to save
    limiter.save(update_fields=['days_left', 'days_used'])


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
    HOME = 'home'

    TYPE_CHOICES = (
        (VACATION, 'Vacation'),
        (DELAY, 'Delay'),
        (SICK, 'Sick'),
        (HOME, 'Home Office')
    )

    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    type_miss = models.CharField(max_length=10, choices=TYPE_CHOICES, default=DELAY)
    approved = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    comment = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{0} {1}".format(self.type_miss, self.pk).title()

    def save(self, *args, **kwargs):
        #Should check if there is a limit for that user/year
        #Update limit on save or return False if limit reached or not set
        if self.type_miss == 'vacation':

            #get specified year
            entered_year = self.to_date.year
            #calculate amount of vacation days
            days = calculate_timedelta(self.from_date, self.to_date)
            #find limiter for that user
            limiters = Limit.objects \
                              .filter(year=entered_year) \
                              .filter(user__id=self.user.id)

            if limiters and limiters.first().days_left >= days:
                update_limiter(days, limiters.first())
                super(Absence, self).save(*args, **kwargs)
                return True
            else:
                #There is no limiter set(found) for this year,
                #  so that we can not save this vacation!
                #Or there are no days left in limiter!
                return False

        else: #sick, delays and home office have no limits
            super(Absence, self).save(*args, **kwargs)
            return True
        