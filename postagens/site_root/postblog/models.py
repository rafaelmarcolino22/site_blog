from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=256)
    resumo = RichTextField()
    conteudo = RichTextField()
    foto = RichTextUploadingField()
    autor = models.ForeignKey(User ,on_delete=models.PROTECT)
    createad_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titulo
# Create your models here.
