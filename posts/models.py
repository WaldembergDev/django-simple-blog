from django.db import models
from accounts.models import CustomUser
from django.utils.text import slugify

class StatusEnumCategories(models.TextChoices):
    ACTIVE = 'Ativo'
    INACTIVE = 'Inativo'

class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)
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
    updated_in = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=StatusEnumPost.choices, default=StatusEnumPost.SKETCH)
    categories = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            # transforma o título em um slug válido
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
