from django.db import models


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    #Кастомизация админки
    def __str__(self):
        return self.id # ("Пользователь %s %s" % (self.email, seil.name)

    #Кастомизация множественного числа и единственного
    class Meta:
        verbose_name=""
        verbose_name_plural=""