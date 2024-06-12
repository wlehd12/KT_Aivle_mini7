from django.db import models

class ChatHistory(models.Model):
    question = models.TextField()
    answer = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Q: {self.question} | A: {self.answer}"
    

class ChatgptHelpaivleqa(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    pclass = models.TextField()
    qa = models.TextField()

    class Meta:
        managed = False
        db_table = 'chatgpt_helpaivleQA'