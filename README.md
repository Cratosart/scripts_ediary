# Приложение для работы с базой данных электронного дневника

### Описание функционала

Скрипт состоит из различных функций которые позволяют решать следующие задачи:

Исправляет оценки `fix_marks`
Удаляет негативные комментарии учителя `delete_prise`
Добавляет похвальные комментарии `create_commendation`

### Запуск скрипта
Для запуска скрипта необходимо импортировать `scripts.py` или скопировать файл и положить в папку с проектом, там где распологается файл `manage.py`.

Пример использования:
```python
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

	name_schoolkid = 'Введите фамилию имя ученика соблюдая регистр'
	name_teacher = 'Введите фамилию имя учителя соблюдая регистр'
	lesson_name = 'Введите название урока с большой буквы'
	schoolkid = Schoolkid.objects.get(full_name__contains=name_schoolkid)
	count_points = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3]).count()
	fix_marks(schoolkid, count_points)
	delete_prise(name_schoolkid)
	praise=random.choice(teacher_praise)
	lesson=Lesson.objects.filter(group_letter__contains='А',
								 year_of_study=6, subject__title=lesson_name).order_by('?').first()
	create_commendation(praise, name_schoolkid, name_teacher, lesson)
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).