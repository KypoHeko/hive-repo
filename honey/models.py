from django.db import models
from django.utils import timezone



class Persona(models.Model):
    email = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    surname = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=32, blank=True)
    age = models.IntegerField(blank=True)
    occupation = models.CharField(max_length=32, blank=True)
    worldview = models.CharField(max_length=32, blank=True)
    quote = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.surname

    @staticmethod
    def _bootstrap(count, gender):
        from mimesis import Personal, Text

        p = Personal('ru')
        t = Text('en')

        for _ in range(count):
            person = Persona(
                email = p.email(),
                password = p.password(length=4),
                surname = p.surname(),
                name = p.name(),
                age = p.age(minimum=18, maximum=35),
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
    chain = models.IntegerField(default=0)

class Community(models.Model):
    name = models.CharField(max_length=256)
    descriptions = models.TextField()
    host = models.IntegerField(default=0)
