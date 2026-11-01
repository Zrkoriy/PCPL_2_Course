from operator import itemgetter


class Student:
    def __init__(self, id, fio, stip, group_id):
        self.id = id
        self.fio = fio
        self.stip = stip
        self.group_id = group_id


class Group:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class StudentGroup:
    def __init__(self, group_id, student_id):
        self.group_id = group_id
        self.student_id = student_id


groups = [
    Group(1, 'группа ИУ5-31Б'),
    Group(2, 'ИУ5-32Б'),
    Group(3, 'учебная группа РТ5-31Б'),
    Group(4, 'ИУ7-33Б'),
]

students = [
    Student(1, 'Иванов', 3000, 1),
    Student(2, 'Петров', 4500, 1),
    Student(3, 'Сидоров', 0, 2),
    Student(4, 'Кузнецов', 3000, 3),
    Student(5, 'Смирнов', 6000, 3),
    Student(6, 'Попов', 4500, 4),
]

students_groups = [
    StudentGroup(1, 1),
    StudentGroup(1, 2),
    StudentGroup(2, 3),
    StudentGroup(3, 4),
    StudentGroup(3, 5),
    StudentGroup(4, 6),
    StudentGroup(3, 1),
    StudentGroup(4, 3),
]


def main():
    one_to_many = [(s.fio, s.stip, g.name)
                   for g in groups
                   for s in students
                   if s.group_id == g.id]

    many_to_many_temp = [(g.name, sg.group_id, sg.student_id)
                         for g in groups
                         for sg in students_groups
                         if g.id == sg.group_id]

    many_to_many = [(s.fio, s.stip, group_name)
                    for group_name, group_id, student_id in many_to_many_temp
                    for s in students if s.id == student_id]

    print('Задание А1')
    res1 = sorted(one_to_many, key=itemgetter(2))
    for x in res1:
        print(x)

    print('\nЗадание А2')
    res2 = []
    for g in groups:
        g_students = list(filter(lambda i: i[2] == g.name, one_to_many))
        if len(g_students) > 0:
            g_stips = [stip for _, stip, _ in g_students]
            res2.append((g.name, sum(g_stips)))
    res2 = sorted(res2, key=itemgetter(1), reverse=True)
    for x in res2:
        print(x)

    print('\nЗадание А3')
    res3 = {}
    for g in groups:
        if 'группа' in g.name:
            g_students = list(filter(lambda i: i[2] == g.name, many_to_many))
            res3[g.name] = [fio for fio, _, _ in g_students]
    for name in res3:
        print(name, res3[name])


if __name__ == '__main__':
    main()
