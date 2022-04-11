def fix_marks(schoolkid, count_points):
	for i in range(count_points):
		mark=Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3])[i]
		mark.points = 5
		mark.save()


schoolkid = Schoolkid.objects.get(full_name__contains='Фролов Иван')
count_points = Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3]).count()
fix_marks(schoolkid, count_points)
Mark.objects.filter(schoolkid=schoolkid, points__in=[2,3]).count()
