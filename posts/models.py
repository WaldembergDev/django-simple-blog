from django.db import models
from accounts.models import CustomUser

class StatusEnumCategories(models.TextChoices):
    ACTIVE = 'Ativo'
    INACTIVE = 'Inativo'

class Categories(models.Model):
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=8, choices=StatusEnumCategories.choices, default=StatusEnumCategories.ACTIVE)

    def __str__(self):
        return self.name

class StatusEnumPost(models.TextChoices):
    SKETCH = 'Rascunho'
    PUBLISHED = 'Publicado'

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    created_in = models.DateTimeField()
    updated_in = models.DateTimeField()
    slug = models.SlugField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=StatusEnumPost.choices, default=StatusEnumPost.SKETCH)
    categories = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
