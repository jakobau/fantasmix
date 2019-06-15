from django.db import models

class Profile(models.Model):
    #user = models.OneToOneField(User)
    CHOICES=[(1, "empty"), (2, "major"), (3, "minor")]
    #scalechoice = models.IntegerField(choices=CHOICES)
