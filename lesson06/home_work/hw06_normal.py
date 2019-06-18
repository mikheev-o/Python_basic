# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Person:
    def __init__(self, surname, name, birth_date = ''):
        self.surname = surname
        self.name = name
        self.birth_date = birth_date
    def fullname(self):
        return(f'{self.surname} {self.name}')

class Pupil(Person):
    def __init__(self, surname, name, parent1, parent2, klass):
        super().__init__(surname, name)
        self.parent1 = parent1
        self.parent2 = parent2
        self.klass = klass
    
    def get_parents(self):
        return self.parent1.fullname(),\
               self.parent2.fullname()

class Teacher(Person):
    def __init__(self, surname, name, subject):
        super().__init__(surname, name)
        self.subject = subject

class Klass:
    def __init__(self, name, teachers):
        self.name = name
        self.teachers = teachers #список преподающих учителей    
    def add_teacher(self, teacher):
        self.teachers.append(teacher)


####################################################

parentA = Person('Иванов', 'Павел')
parentB = Person('Иванова', 'Мария')
parentC = Person('Сергеев', 'Денис')
parentD = Person('Платонова', 'Клара')
parentE = Person('Кромвель', 'Кирилл')
parentF = Person('Кромвель', 'София')

teacher1 = Teacher('Иванов', 'Павел', 'география')
teacher2 = Teacher('Ге', 'Пётр', 'математика')
teacher3 = Teacher('Петров', 'Григорий', 'биология')
teacher4 = Teacher('Ян', 'Ин', 'химия')
teacher5 = Teacher('Черепанов', 'Павел', 'физика')
teacher6 = Teacher('Клот', 'Серафим', 'пение')
teacher7 = Teacher('Парве', 'Платон', 'труд')
teacher8 = Teacher('Чижиков', 'Василий', 'литература')

klass1 = Klass('4А', [teacher1, teacher2, teacher6, teacher7, teacher8])
klass2 = Klass('5А', [teacher1, teacher3, teacher8, teacher6, teacher7])
klass3 = Klass('6А', [teacher1, teacher3, teacher8, teacher4, teacher5, teacher7])
klass4 = Klass('6Б', [teacher1, teacher3, teacher8, teacher4, teacher5, teacher6])

pupil1 = Pupil('Иванов', 'Саша', parentA, parentB, klass1)
pupil2 = Pupil('Сергеева', 'Рита', parentC, parentD, klass2)
pupil3 = Pupil('Кромвель', 'Валя', parentE, parentF, klass2)
pupil4 = Pupil('Иванова', 'Маша', parentA, parentB, klass3)
pupil5 = Pupil('Сергеева', 'Грета', parentC, parentD, klass3)


klasses = [klass1,klass2,klass3,klass4] ## это как бы школа
pupils = [pupil1,pupil2,pupil3,pupil4,pupil5] ## это список учеников


def klass_list(name):
    for p in pupils:
        if p.klass.name == name:
            print(p.fullname())

### 1. Список одного класса
kl_name = '5А'
print(f'\nСписок класса {kl_name}:')
klass_list(kl_name)

### 2
print('\nСписок всех классов:')
for k in klasses:
    klass_list(k.name)

### 3
print(f'\nСписок предметов ученика {pupil1.fullname()}:')
for t in pupil1.klass.teachers:
    print(t.subject)

### 4
print(f'\nРодители ученика {pupil2.fullname()}:')
print(pupil2.get_parents())

### 5
print(f'\nСписок учителей класса {klass3.name}:')
for t in klass3.teachers:
    print(f'{t.fullname()}, {t.subject}')
