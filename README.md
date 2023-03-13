Добрый день хочу представить вам свой сервис с вакансиями и соискателями!

### Прошу меня извинить, но из-за непредвиденных обстоятельств я смог уделить проекту порядка 7 часов,
### и часть функционала в данный момент отсутствует.








API реализован на основе  DRF.

### **Запуск проекта в dev-режиме**
Инструкция для OS windows и утилиту git bash.


1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/Knoxvillys/hh_test.git
```

```
cd api_yatube_final
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py создать скрипт миграции:
```
python manage.py makemigrations 
```

5. папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```

6. Зарегестрировать супер пользователя(
Базу я отправил на удаленный репозиторий в котором уже есть Admin
login: admin password: admin
)
```
python manage.py createsuperuser
```

8. папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

### **В проекте реализованный администраторский интерфейс.**
```
http://127.0.0.1:8000/admin
```



### **Создание "Резюме"**
Обратитесь по ссылке
Будет возможность сделать POST и создать резюме:
```
http://127.0.0.1:8000/HomeHm/my
```

Например:
```
 {
        "id": 1,
        "name": "Тюрин",
        "surname": "Никита",
        "patronymic": "Вадимович",
        "phoneNumber": "+79835056491",
        "secondPhoneNumber": "+79835056491",
        "about_me": "Я ваще классный",
        "image": "http://127.0.0.1:8000/image/%D0%A4%D0%BE%D1%82%D0%BE_4hSy3Qg.jpg",
        "salary": 123,
        "company": "ООО \"Рога и копыта\"",
        "results_of_work": "Веселились",
        "start_date": "2023-03-02T15:09:48Z",
        "end_date": "2023-03-02T15:09:51Z",
        "author": 1
    }
```

Так же возможно пользоваться стандартными представлениями DRF в браузере.

Изменение:
```
http://127.0.0.1:8000/HomeHm/patch/<int:pk>
```
Удалить:
```
http://127.0.0.1:8000/HomeHm/del/<int:pk>
```
Получить все Резюме:
```
http://127.0.0.1:8000/HomeHm
```


### **Создание "Вакансии"**
Обратитесь по ссылке
Будет возможность сделать POST и создать резюме:
```
http://127.0.0.1:8000/home/my
```
        "id": 1,

        "company": { <-- 'Эту часть заполнять не нужно она должна быть выбрана в HTML свою компанию
            "id": 1,
            "employer_name": "ООО \"абв\"",
            "number_of_employees": 123,
            "address": "улица Пушкина дом 1к",
            "phoneNumber": "+79835056191",
            "secondPhoneNumber": "+79835056192",
            "image": "http://127.0.0.1:8000/image/%D0%98%D0%9D%D0%9D_%D0%A2%D1%8E%D1%80%D0%B8%D0%BD_Usme7Ez.jpg"
        },           <-- 'Эту часть заполнять не нужно она должна быть выбрана в HTML свою компанию

        "about_compony": "Приходи к нам мы охотимся за газировкой",
        "salary": 123,
        "specialist": "Backend-разработчик"
Изменение:
```
http://127.0.0.1:8000/home/patch/<int:pk>
```
Удалить:
```
http://127.0.0.1:8000/home/del/<int:pk>
```
Получить все Вакансии:
```
http://127.0.0.1:8000/home
```



Я успел поставить Аутентификацию через djoser но не успел сделать ни одной HTML. и временно отключил возможность,
однако отзыв на вакансию все еще имеет все атрибуты для работы с правами.

При запресе по адресу:
```
http://127.0.0.1:8000/v1/follow/
```
Однако в данный момент она не даст вам доступа, так-как вы не можете зарегистрироваться из-за отсутствия 
пути для регистрации.

В теории оба пользователя "Соискатель", "Работодатель", могут увидеть кто откликнулся, Но я не доделал
возможность залогиниться.

Можно посмотреть зависимости.
```
pip freeze
```
