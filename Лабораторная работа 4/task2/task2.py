def get_count_char(str_):
    symbol_num = {
    }
    string=str_.lower()
    for s in string:
        if symbol_num.get(s)==None and s.isalpha():
            symbol_num.update({s: 1})
        elif s.isalpha():
            symbol_num[s]+=1
    return symbol_num

def get_count_percentage(str_):
    symbol_num = get_count_char(str_)
    for key in symbol_num.keys():
        symbol_num[key] = round(symbol_num[key]/sum(symbol_num.values())*100, 1)
    return symbol_num

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(get_count_percentage(main_str))