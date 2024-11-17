from django.db import models
# Create your models here.

class Articles(models.Model):
    # это вторичный ключ, связывающий варианты ответа с конкретный вопросом
    article_title = models.CharField(max_length=200)  # здесь описание ответа на вопрос
    article_content = models.CharField(max_length=1000)  # здесь описание ответа на вопрос
    pub_date = models.DateTimeField("дата публикации")
    def __str__(self):
        return self.article_content
