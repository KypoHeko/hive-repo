from django.db import models

class Persona(models.Model):
    surname = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    occupation = models.CharField(max_length=32)
    worldview = models.CharField(max_length=32)
    quote = models.CharField(max_length=128)

    #Для работы через shell
    #def __str__(self):
    #    return self.surname

    #def __init__(self, **kwargs):
    #    super(Persona, self).__init__(**kwargs)

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

