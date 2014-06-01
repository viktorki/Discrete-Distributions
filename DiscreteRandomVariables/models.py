from django.db import models

class Problem(models.Model):
    problem_title = models.CharField()
    problem_statement = models.TextField()
    solution = models.TextField()
    distribution_id = models.IntegerField()
