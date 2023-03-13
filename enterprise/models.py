from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField # Форма для телефонного номера

#from markitup.fields import MarkupField # Импорт виджета для редактирования текста
#from markdown import markdown


class Employer(models.Model):
    '''
    Модель зарегистрированной компании.
    '''
    employer_name = models.CharField(max_length=100) # Название работодателя
    number_of_employees = models.IntegerField(null=True) # кол-во работников
    address = models.CharField(max_length=100) # Адрес
    phoneNumber = PhoneNumberField(unique=True, null=False, blank=False) # Основной номер телефона
    secondPhoneNumber = PhoneNumberField(null=True, blank=True) # Запасной номер телефона
    image = models.ImageField(upload_to='image', null=True) # Изображение
    user = models.ForeignKey(User, verbose_name='Работодатель', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.employer_name


class About(models.Model):
    '''
    Модель вакансии.
    '''
    BACKEND = 'Backend-разработчик'
    FRONTEND = 'Frontend-разработчик'
    DATA_SCIENCE = 'Data Science'
    DEFAULT = 'Разработчик'
    DECISION = [
        (BACKEND, 'Backend-разработчик'),
        (FRONTEND, 'Frontend-разработчик'),
        (DATA_SCIENCE, 'Data Science')
    ]
    
    about_compony = models.TextField(max_length=300)  # О вакансии
    salary = models.IntegerField(null=True)  # Сумма вознаграждения
    specialist = models.CharField(max_length=40, choices=DECISION, default=DEFAULT)  # Выбор специалиста
    company = models.ForeignKey(Employer, verbose_name='Компания', on_delete=models.CASCADE) # Связь с компанией
    
