""" Вы уже научились работать со строками более глубоко и теперь у вас есть полный набор 
инструментов для обработки строк с помощью Python.

С помощью функции zip, по аналогии с примером из теории, создайте словарь TRANS для транслитерации. 
Создавайте словарь TRANS вне функции translate

Напишите функцию translate, которая проводит транслитерацию кириллического алфавита на латинский.

Функция translate:

принимает на вход строку и возвращает строку;
проводит транслитерацию кириллических символов на латиницу;
Пример работы:

print(translate("Дмитрий Коробов"))  # Dmitrij Korobov
print(translate("Александр Иванович"))  # Aleksandr Ivanovich
Примечание: В задаче, при создании словаря TRANS, код TRANS[ord(c.upper())] = l.title() 
будет считаться не правильным, а TRANS[ord(c.upper())] = l.upper() — правильным. 
Это компромисс, так как в первом случаем мы учитываем заглавные буквы, 
а во втором — правильно, если имя будет все заглавными буквами. Чтобы не усложнять задачу, 
принято как в документах — все имя печатается заглавными. """

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}

# Create dict trans with help of zip()
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

#print("чаша".translate(TRANS))  # chasha
#print("ЧАША".translate(TRANS))  # CHASHA    
#print(TRANS)
    


def translate(name):
    return name.translate(TRANS)

print(translate("Сергій"))
