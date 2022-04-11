# Приложение для работы с базой данных электронного дневника

Скрипты состоят из различных функций которые позволяют решать следующие задачи:

### Как исправить оценки

запустить консоль управления проектом shell:

```
python manage.py shell
```

скопировать в shell следующий скрипт:
```
from datacenter.models import Lesson
from datacenter.models import Mark
from datacenter.models import Schoolkid
from django.core.exceptions import ObjectDoesNotExist


def fix_marks(schoolkid, count_points):
	for i in range(count_points):
		mark=Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])[i]
		mark.points = 5
		mark.save()

try:
	schoolkid = Schoolkid.objects.get(full_name__contains='Фролов Иван')
except ObjectDoesNotExist:
	print(введено не корректное значение)
count_points = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3]).count()
fix_marks(schoolkid, count_points)
Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3]).count()

```

что бы исправить оценки друзей нужно заменить full_name__contains='ФАМИЛИЯ ИМЯ ДРУГА'

### Удалить жалобы учителя
запустить консоль управления проектом shell:

```
python manage.py shell
```

```
comment=Chastisement.objects.filter(schoolkid=Schoolkid.objects.get(full_name__contains='Шаров Еремей'))
comment.delete()
```
full_name__contains = 'вписать фамилию имя друга или себя'



### Внести похвалу
запустить консоль управления проектом shell:

```
python manage.py shell
```

```
import random


def create_commendation(praise, name_schoolkid, name_teacher, lesson):
	Commendation.objects.create(teacher=Teacher.objects.get(full_name__contains=name_teacher), subject=lesson.subject, schoolkid=Schoolkid.objects.get(full_name__contains=name_schoolkid), created=lesson.date, text=praise)


teacher_praise=['Молодец!',
'Отлично!',
'Хорошо!',
'Гораздо лучше, чем я ожидал!',
'Ты меня приятно удивил!',
'Великолепно!',
'Прекрасно!',
'Ты меня очень обрадовал!',
'Именно этого я давно ждал от тебя!',
'Сказано здорово – просто и ясно!',
'Ты, как всегда, точен!',
'Очень хороший ответ!',
'Талантливо!',
'Ты сегодня прыгнул выше головы!',
'Я поражен!',
'Уже существенно лучше!',
'Потрясающе!',
'Замечательно!',
'Прекрасное начало!',
'Так держать!',
'Ты на верном пути!',
'Здорово!',
'Это как раз то, что нужно!',
'Я тобой горжусь!',
'С каждым разом у тебя получается всё лучше!',
'Мы с тобой не зря поработали!',
'Я вижу, как ты стараешься!',
'Ты растешь над собой!',
'Ты многое сделал, я это вижу!',
'Теперь у тебя точно все получится!']

praise=random.choice(teacher_praise)
name_schoolkid = 'Фролов Иван'
name_teacher = 'Селезнева Майя'

lesson=Lesson.objects.filter(group_letter__contains='А',year_of_study=6, subject__title='Музыка').order_by('?').first()
create_commendation(praise, name_schoolkid, name_teacher, lesson)
```

name_schoolkid = 'Фролов Иван' - заменить фамилию имя на человека кому нужны хорошие отзывы учителей
subject__title='Музыка' - заменить на нужный предмет
name_teacher = 'Селезнева Майя' - заменить на учителя предмета


### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).