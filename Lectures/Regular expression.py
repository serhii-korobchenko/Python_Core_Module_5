""" Составление регулярных выражений — это отдельная большая тема достойная отдельного изучения. Регулярные выражения состоят из блоков и модификаторов.

Примером блока может быть:

[a,b,c,z] в квадратные скобки заключают набор символов, из которых должна состоять строка
. любой символ
\d число или [0-9]
\D не число, или [^0-9]
\s любой символ, обозначающий пробел или табуляцию, перенос строки и пр.
\w любое число или буква, включая нижнее подчеркивание, или [a-zA-Z0-9_]
\W не буква, не число и не нижнее подчеркивание
Модификаторы могут указывать на число повторений блока в выражении, например:

? 0 или 1 раз
+ 1 или более раз
* 0 или более раз
{n} строго n раз (n целое число)
{n, m} от n до m раз
Комбинируя блоки и выражения, можно составить выражения для ваших нужд:

Регулярка	                 Её смысл	
simple text	                 В точности текст «simple text»	
\d{5}	                     Последовательности из 5 цифр \d означает любую цифру {5} — ровно 5 раз	
\d\d/\d\d/\d{4}	             Даты в формате ДД/ММ/ГГГГ (и прочие куски на них похожие, например, 98/76/5432)	
\b\w{3}\b	                 Слова в точности из трёх букв \b означает границу слова (с одной стороны буква, а с другой — нет) \w — любая буква, {3} — ровно три раза	
[-+]?\d+	                 Целое число, например, 7, +17, -42, 0013 (возможны ведущие нули) [-+]? — либо -, либо +, либо пусто \d+ — последовательность из 1 или более цифр	
`[-+]?(?:\d+(?:.\d*)?	     .\d+)(?:[eE][-+]?\d+)?`	Действительное число, возможно в экспоненциальной записи. Например, 0.2, +5.45, -.4, 6e23, -3.17E-14. """