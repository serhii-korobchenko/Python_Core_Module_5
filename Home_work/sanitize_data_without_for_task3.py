""" Ваша компания проводит маркетинговые кампании с помощью SMS рассылок. 
Автоматический сбор телефонных номеров с базы данных формирует определенный список. 
Но клиенты оставляют свои номера в произвольном виде:

    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
Сервис рассылок прекрасно понимает и может отправить SMS-ку клиенту, 
только если телефонный номер содержит цифры. Необходимо реализовать функцию 
sanitize_phone_number, которая будет принимать строку с телефонным номером 
и нормализовать его, т.е. будет убирать символы (, -, ), + и пробелы.

Результат:

380501233234
0503451234
0508889900
380501112222
380501112211 """


import re
def sanitize_phone_number(phone):
    
    
    new_format = re.findall('\d', phone)
        
    res_string = ''.join(new_format) # List to string
    #print (res_string)
    return res_string

print (sanitize_phone_number("    +38(050)123-32-34"))