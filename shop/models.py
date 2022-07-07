from django.db import models

#dev1 form w_st1 form a1 will develop here

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    