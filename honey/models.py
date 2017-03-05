from django.db import models
from django.utils import timezone

class Persona(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    occupation = models.CharField(max_length=32)
    worldview = models.CharField(max_length=32)
    quote = models.CharField(max_length=128)

    #Для работы через shell
    def __str__(self):
        return 'self.id'

    @staticmethod
    def _bootstrap(count, locale, gender):
        from elizabeth import(
            Personal,
            Text,
            )

        p = Personal(locale)
        t = Text(locale)

        for _ in range(count):
            person = Persona(
                    surname = p.surname(),
                    name = p.name(),
                    age = p.age(maximum=35),
                    occupation = p.occupation(),
                    worldview = p.worldview(),
                    quote = t.quote(),
                )

            person.save()

class Message(models.Model):
    sender = models.IntegerField()
    recepient = models.IntegerField()
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

class Community(models.Model):
    name = models.CharField(max_length=256)
    descriptions = models.TextField()
