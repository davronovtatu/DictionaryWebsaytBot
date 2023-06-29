from django.db import models



class Word(models.Model):
    uzb_word=models.CharField(max_length=300)
    eng_word=models.CharField(max_length=300)



    def __str__(self):
        return f"{self.uzb_word} | {self.eng_word}"



class User(models.Model):
    id=models.AutoField(primary_key=True)
    full_name=models.CharField(verbose_name="To'liq Ism ",max_length=250)
    username=models.CharField(verbose_name="Username",max_length=250,null=True)
    telegram_id=models.BigIntegerField(verbose_name="Telegram Id",unique=True,default=1)


    def __str__(self):
        return f"{self.id} | {self.full_name} | {self.username} | {self.telegram_id}"













