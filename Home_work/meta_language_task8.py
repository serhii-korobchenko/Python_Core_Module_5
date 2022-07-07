""" В прошлом модуле мы работали с системой оценок ECTS. 
Напишите функцию formatted_grades, которая принимает на вход словарь оценивания 
студентов по предмету следующего вида:

students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
И возвращает список отформатированных строк, чтобы при выводе следующего кода:

for el in formatted_grades(students):
    print(el)
Получалась следующая таблица:

   1|Nick      |  A  |  5
   2|Olga      |  B  |  5
   3|Mike      | FX  |  2
   4|Anna      |  C  |  4
первый столбец — ширина 4 символа, выравнивание по правому краю
второй столбец — ширина 10 символов, выравнивание по левому краю
третий и четвертый столбец — ширина 5 символов и выравнивание по центру
вертикальный символ | не входит в ширину столбца """


grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
students_our = {'Nick': 'A', 'Olga': 'B', 'Boris': 'FX', 'Anna': 'C'}

def formatted_grades(students):
    res_list = []
    count = 0
    for key, value in students.items():
        count +=1
        #print(value)
        digit_grade = grades[value]
        #print(digit_grade)
        width = 5
        res =  '{:>4}|{:<10}|{:^5}|{:^5}'.format(count, key, value, digit_grade)
        res_list.append(res)
        #print (type(res_list))
    print (res_list)
    return res_list

for el in formatted_grades(students_our):
    print(el)
    

