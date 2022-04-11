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
