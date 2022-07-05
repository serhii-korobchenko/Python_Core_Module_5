""" Вернемся к нашей задаче с телефонными номерами. 
Компания расширяется и вышла на рынок Азии. 
Теперь в списке приходят телефоны разных стран. 
Каждая страна имеет свой телефонный код .

Компания работает со следующими странами

Страна	Код ISO	Префикс
Japan	JP	+81
Singapore	SG	+65
Taiwan	TW	+886
Ukraine	UA	+380
Чтобы мы могли корректно выполнить маркетинговую SMS кампанию, необходимо выдать для 
каждой страны свой список телефонных номеров.

Напишите функцию get_phone_numbers_for_сountries, которая будет:

Принимать список телефонных номеров.
Санитизировать (нормализовать) полученный список телефонов клиентов с помощью 
нашей функции sanitize_phone_number.
Сортировать телефонные номера по указанным в таблице странам.
Возвращать словарь со списками телефонных номеров для каждой страны в следующем виде:
{
    "UA": [<здесь список телефонов>],
    "JP": [<здесь список телефонов>],
    "TW": [<здесь список телефонов>],
    "SG": [<здесь список телефонов>]
}
Если не удалось сопоставить код телефона с известными, этот телефон должен быть 
добавлен в список словаря с ключом "UA". """


Country_dicts = [
                {'Country': 'Japan', 'ISO': 'JP', 'Prefix': '81'},
                {'Country': 'Singapore', 'ISO': 'SG', 'Prefix': '65'},
                {'Country': 'Taiwan', 'ISO': 'TW', 'Prefix': '886'},
                {'Country': 'Ukraine', 'ISO': 'UA', 'Prefix': '380'}]


def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

def get_phone_numbers_for_countries(list_phones):
    result_dict = {}
    result_list = []
    ukraine_list = []
    
    # initial sorting
    for item in list_phones:
        
        flag = 0
        sun_number = sanitize_phone_number(item)
        for element in Country_dicts:
            if sun_number.startswith(element["Prefix"]):
                print(element["Country"])
                result_list.append(sun_number)
                result_dict.update({element["ISO"]: result_list})

                flag +=1
        if flag == 0:
            result_list.append(sun_number)
            result_dict.update({element["ISO"]: result_list})
            ukraine_list.append(sun_number)
    
    
    # internal sorting
    new_result_dict = {} 
    for key, value in result_dict.items():
        new_value = []  
        for element in Country_dicts:

            if element["ISO"] == key:
                prefix = element["Prefix"]
                iso = element["ISO"]
                #print(prefix)
                
        for el in value:
            if el.startswith(prefix):
                new_value.append(el)
                #print(new_value)
            


        new_result_dict.update({iso: new_value})  
    
    new_result_dict["UA"] = new_result_dict["UA"] + ukraine_list 
     # We need add ukraine_list
    
    return  new_result_dict


""" print (get_phone_numbers_for_countries(["    +38(050)123-32-34",
                                         "     0503451234",
                                         "(050)8889900",
                                          "38050-111-22-22",
                                           "38050 111 22 11   "])) """



print (get_phone_numbers_for_countries(["    +38(050)123-32-34",
                                         "     +810503451234",
                                         "(050)8889900",
                                          "38050-111-22-22",
                                           "38050 111 22 11   "]))

