from django.db import models

# Create your models here.

class BlogPost(models.Model):
  title       = models.CharField(max_length=200, blank=False, null=False)
  preface     = models.TextField(blank=False, null=False)
  description = models.TextField(blank=False, null=False)


class BlogComment(models.Model):
  nameFamily = models.CharField(max_length=50, blank=False, null=False)
  message    = models.TextField(blank=False, null=False)