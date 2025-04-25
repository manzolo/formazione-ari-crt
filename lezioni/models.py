from django.db import models

class Lezione(models.Model):
    numero = models.IntegerField()
    titolo = models.CharField(max_length=200)
    url_video = models.URLField()
    file_slide = models.FileField(upload_to='documenti/slide/')
    file_domande = models.FileField(upload_to='documenti/domande/')
    file_risposte = models.FileField(upload_to='documenti/risposte/')

    def __str__(self):
        return self.titolo