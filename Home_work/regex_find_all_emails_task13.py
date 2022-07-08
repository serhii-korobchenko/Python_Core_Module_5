""" Теперь мы потренируемся писать полезные регулярные выражения. Напишите регулярное выражение для 
функции find_all_emails, которая будет в тексте (параметр text) находить все email и 
возвращать список полученных из текста совпадений.

В целях упрощения примем, что:

алфавит, используемый для названия email, — английский
префикс (все, что находится до символа @) начинается с латинской буквы и может 
содержать любое число или букву, включая нижнее подчеркивание и символ точки, 
состоит минимум из двух символов
суффикс письма (все, что находится после символа @) состоит только из букв английского алфавита, 
состоит из двух частей, разделенных точкой, и доменное имя верхнего уровня не может 
быть меньше двух символов (все, что после точки)
Данное регулярное выражение ни в коей мере не претендует на покрытие всех возможных 
вариантов email.

При выполнении этого задания мы рекомендуем использовать следующий сервис для проверок 
регулярных выражений regex101. """


import re

text = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net" #7

def find_all_emails(text):
    result = re.findall(r"[a-zA-Z]{1}[\w\.]+@[a-zA-Z]*\.[a-z]{2,}", text)
    return result
    
print(find_all_emails(text))



""" Функция find_all_emails возвращает неправильный результат: 
['Ima.Fool@iana.org', '***Ima.Fool@iana.o'***, '***1**Fool@iana.org***', 'first_last@iana.org', 
'middle.last@iana.or', '***a@test.com'***, 'abc111@test.com.net']. 

Ожидалось, что функция find_all_emails при получении параметра 

'Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or 
a@test.com abc111@test.com.net'


 вернет следующий список 

['Ima.Fool@iana.org', 'Fool@iana.org', 'first_last@iana.org', 'first.middle.last@iana.or', 
'abc111@test.com'] """

""" cool@api.io cool@api.i first.middle.last@iana.or a2@test.com a3@test.com.io 222111@test.com' 

['cool@api.io', 'first.middle.last@iana.or', 'a2@test.com', 'a3@test.com']
 """