from django.db import models

# Create your models here.

class ChatgptHelpaivleqa(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    pclass = models.TextField()
    qa = models.TextField()

    class Meta:
        managed = False
        db_table = 'chatgpt_helpaivleQA'