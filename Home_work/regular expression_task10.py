""" Напишите функцию find_word, которая принимает два параметра: первый text и второй word. 
Функция выполняет поиск указанного слова word в тексте text с помощью функции search и 
возвращает словарь.

При вызове функции:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor to the 
    ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат должен быть следующего вида при совпадении:

{
    'result': True,
    'first_index': 34,
    'last_index': 40,
    'search_string': 'Python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, 
    as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
}
где

result — результат поиска True или False
first_index — начальная позиция совпадения
last_index — конечная позиция совпадения
search_string — часть строки, в которой было совпадение
string — строка, переданная в функцию
Если совпадений не обнаружено:

print(find_word(
    "Guido van Rossum began working on Python in the late 1980s, as a successor
     to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
    "Python"))
Результат:

{
    'result': False,
    'first_index': None,
    'last_index': None,
    'search_string': 'python',
    'string': 'Guido van Rossum began working on Python in the late 1980s, 
    as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
} """

import re


def find_word(text, word):
    dict_res = {
            'result': None,
            'first_index': None,
            'last_index': None,
            'search_string': None,
            'string': None
          }
    dict_res['search_string'] = word
    dict_res['string'] = text
    result = re.search(word, text)
    if result == None:
        dict_res['result'] = False
    else:
        dict_res['result'] = True
        first_ind, last_ind = (result.span())
        dict_res['first_index'] = first_ind
        dict_res['last_index'] = last_ind
    

    return dict_res
    
    
print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.","Python"))

#print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "python"))

