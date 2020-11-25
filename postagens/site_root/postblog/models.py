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




class Cadas(models.Model):

    STATUS = (
        ('doing', 'DOING'),
        ('done', 'DONE'),
    )

    nome = models.CharField(max_length=256)
    idade = models.CharField(max_length=3)
    cidade = models.CharField(max_length=30)


    done = models.CharField(
        max_length=5,
        choices=STATUS
    )

    