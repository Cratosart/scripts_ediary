import random
from datacenter.models import *


def fix_marks(schoolkid):
	marks=Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])
	for mark in marks:
		mark.points = 5
		mark.save()


def create_commendation(praise, name_schoolkid, name_teacher, lesson):
	Commendation.objects.create(teacher=Teacher.objects.get(full_name__contains=name_teacher),
								subject=lesson.subject, schoolkid=Schoolkid.objects.get(full_name__contains=name_schoolkid),
								created=lesson.date,
								text=praise)


def delete_prise(name_schoolkid):
    comment = Chastisement.objects.filter(schoolkid=Schoolkid.objects.get(full_name__contains=name_schoolkid))
    comment.delete()


def main():
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


if __name__ == '__main__':
    main()

