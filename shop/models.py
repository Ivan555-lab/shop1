from django.db import models

#dev1 form w_st1 form a1 will develop here

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categores'

    def __str__(self):
        return self.name

    