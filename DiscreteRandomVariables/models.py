from django.db import models

class Problem(models.Model):
    problem_title = models.CharField(max_length = 128)
    problem_statement = models.TextField()
    solution = models.TextField()
    distribution_id = models.IntegerField()
    distribution_parameter1 = models.FloatField()
    distribution_parameter2 = models.FloatField()
    distribution_parameter3 = models.FloatField()
