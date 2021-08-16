from django.db import models


class Agent(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)


class Lead(models.Model):
    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter'),
    )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

    contacted = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    profile_picture = models.ImageField(blank=True, null=True)
    special_files = models.FileField(blank=True, null=True)




