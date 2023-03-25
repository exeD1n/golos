from django.db import models

# Create your models here.
# password bootstrap1234

class All(models.Model):
    FORM_OF_Study = (
        ('У', 'Удаленная форма обучения'),
        ('З', 'Заочная форма обучения'),
        ('О', 'Очная форма обучения'),
    )
    fullName = models.CharField('ФИО', max_length=250)
    mail = models.EmailField('Почта обучаемого', max_length=250)
    formOfStudy = models.CharField('Форма обучения',max_length=1, choices=FORM_OF_Study)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True, verbose_name = 'Группа')
    courseOfStudy = models.ForeignKey('CourseOfStudy', on_delete=models.PROTECT, null=True, verbose_name = 'Номер курса')
    hilary_id = models.ForeignKey('Hilary', on_delete=models.PROTECT, null=True, verbose_name = 'Сдаваемая сессия')
    
    def __str__(self):
        return self.fullName
    
    class Meta:
        verbose_name = 'Запись с учеником'
        verbose_name_plural = 'Записи с учениками'
    
    
class Group(models.Model):
    name = models.CharField('Название группы', max_length=250)
    directionStudy = models.CharField('Номер направления', max_length=250)
    
    def __str__(self):
        return self.name 
    
    class Meta:
        verbose_name = 'Название группы и направление'
        verbose_name_plural = 'Названия групп и направлений'
        

class CourseOfStudy(models.Model):
    name = models.CharField('Номер курса', max_length=250)
    
    def __str__(self):
        return self.name   
    
    class Meta:
        verbose_name = 'Номер курса'
        verbose_name_plural = 'Номера курсов'
   
    
class Hilary(models.Model):
    name = models.CharField('Название сдаваемой сессии', max_length=250)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Название сессии'
        verbose_name_plural = 'Названия сессий'
