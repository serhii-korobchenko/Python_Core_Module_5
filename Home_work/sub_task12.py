""" В шестой задаче мы писали функцию is_spam_words, которая определяла, есть или нет стоп-слова 
в тексте сообщения. Давайте пойдем дальше и применим функцию sub модуля re для замены 
указанных в списке стоп-слов на некоторый шаблон. Например, все "плохие" слова будем заменять 
звездочками. Напишите функцию replace_spam_words, которая принимает строку (параметр text), 
проверяет её на содержание запрещённых слов из списка (параметр spam_words), и возвращает 
результат строку, но вместо запрещенных слов, подставлен шаблон из *, причем длина шаблона 
равна длине запрещенного слова. Определить нечувствительность к регистру стоп-слов. """



import re

check_text = 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn '

spam_words_global = ['began', 'Python']

def replace_spam_words(text, spam_words):
    result = text
    for item in spam_words:
        fill_ver = '*' * len(item)
        pattern = item
        result = re.sub(pattern, fill_ver, result, 0, re.IGNORECASE)
        #result = re.sub(pattern, fill_ver, result)


    return result



print(replace_spam_words(check_text, spam_words_global))