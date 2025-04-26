from django.db import models

class Lezione(models.Model):
    numero = models.IntegerField()
    titolo = models.CharField(max_length=200)
    data_lezione = models.DateField(null=True, blank=True)
    url_video = models.URLField()
    file_slide = models.FileField(upload_to='documenti/slide/', null=True, blank=True)
    file_domande = models.FileField(upload_to='documenti/domande/', null=True, blank=True)
    file_risposte = models.FileField(upload_to='documenti/risposte/', null=True, blank=True)

    def __str__(self):
        return self.titolo