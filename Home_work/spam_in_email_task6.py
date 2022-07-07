""" Рассмотрим задачу на проверку спама в email письме или фильтрацию запрещенных слов в сообщении.

Пусть функция is_spam_words принимает строку (параметр text), проверяет её на содержание 
запрещённых слов из списка (параметр spam_words), и возвращает результат проверки: True, 
если есть хоть одно слово из списка, и False, если в тексте стоп-слов не обнаружено.

Слова в параметре text могут быть в произвольном регистре, а значит функция is_spam_words, 
при поиске запрещённых слов, регистронезависима и весь текст должна сводить к нижнему регистру. 
Для упрощения, будем считать, что в строке присутствует только одно запрещенное слово.

Предусмотреть третий параметр функции space_around, который по умолчанию равен False. 
Он отвечает за то, что функция будет искать отдельное слово или нет. 
Слово считается стоящим отдельно, если слева от слова находится символ пробела 
или оно расположено в начале текста, а справа от слова находится пробел или символ точки.

Например, в тексте мы ищем слово "лох". То в слове "Молох" вызов и результат будет следующим:

print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
т.е. во втором случае слово не отдельное и является частью другого.

В этом примере, функция вернет True в обоих случаях.

print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True """

check_text = 'Например, в тексте мы ищем слово лох. То в слове Молох вызов и результат будет следующим.'

spam_words = ['лох', 'екс']

def is_spam_words(text, spam_words, space_around=False):
    check_result = False
    print(text.lower())
    
    for item in spam_words:
        print(item.lower())
        
        if text.find(item) != -1:
            if space_around:   # _|(in begining) word _|.   
                left_pos = text.index(item)
                right_pos = left_pos + len(item)-1
                print(text[left_pos-1], text[right_pos+1])
                if (text[left_pos-1] == ' ' or left_pos == 0) and (text[right_pos+1] == ' ' or text[right_pos+1] == '.'):
                    print('Here is spam')
                    check_result = True
                else:
                    print('Here is no spam')
            else:
                print('Here is spam')
                check_result = True
        else:
            print('Here is no spam')

    
    return check_result
    # Use loower method for to make equel sourse and input


print(f"Result of is_spam_words: {is_spam_words(check_text, spam_words, True)}")