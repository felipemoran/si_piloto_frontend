# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    titulo = models.CharField("Título", max_length=50)
    conteudo = models.TextField("Conteúdo")
    autor = models.ForeignKey(User, related_name='autor_post')
    curtida = models.ManyToManyField(User, blank=True, through="Status_curtida")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo.encode('utf-8')


class Perfil_user(models.Model):
    user = models.OneToOneField(User)

    class Meta:
        verbose_name = "Perfil_user"
        verbose_name_plural = "Perfis_users"

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Comentario(models.Model):
    autor = models.ForeignKey(User, related_name='autor_curtida')
    post = models.ForeignKey(Post)
    texto = models.TextField()

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"

    def __str__(self):
        return self.autor.username + ' ' + ' -> ' + self.post.titulo


class Status_curtida(models.Model):
    curtiu = models.BooleanField(default=False)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    class Meta:
        verbose_name = "Status_curtida"
        verbose_name_plural = "Status_curtidas"

    def __str__(self):
        return self.user.username + ' -> ' + self.post.titulo.encode('utf-8')

