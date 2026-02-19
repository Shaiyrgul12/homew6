from django.db import models



class MyInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя пользователя")
    photo = models.ImageField(upload_to='myinfo/', verbose_name="Фото")
    profession = models.CharField(max_length=100, verbose_name="Профессия")
    age = models.IntegerField(verbose_name="Возраст")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Моя информация"
        verbose_name_plural = "Мои данные"


class CompanyInfo(models.Model): 
    name = models.CharField(max_length=50, verbose_name= "Название компании")
    about = models.TextField(verbose_name="Описание")
    phone = models.CharField(max_length=30,verbose_name="Контакты")
    email = models.EmailField(verbose_name="Email")
    address = models.CharField(max_length=80,verbose_name="Адрес")
    working_hours = models.CharField(max_length=100,verbose_name="Рабочие часы")
    locate = models.URLField(verbose_name="Ссылка на карту")
    instagram = models.URLField(verbose_name="Ссылка на инстаграм")
    facebook = models.URLField(verbose_name="Ссылка на фейсбук")
    youtube = models.URLField(verbose_name="Ссылка на ютуб")
    whatsapp = models.URLField(verbose_name="Ссылка на ватсап")
    telegram = models.URLField(verbose_name="Ссылка на телеграм")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Информация о компании"
        verbose_name_plural = "Информация о компаниях"
    
   
