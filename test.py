#import csv
#with open('test_data.csv', newline='', encoding='utf-8') as f:
#    reader = csv.reader(f)
#    for row in reader:
#        print(row)


import pandas as pd
data = pd.read_csv("test_data.csv")


#сортировка
#print(data.loc[data['role']=='manager'][['role','text']])

#фильтры
print(data[data.text.str.contains('здравствуйте')])


#Вывод приветсвия от менеджера -использовала сортировку по столбцу + фильтр по тексту
print(data.loc[data['role']=='manager'][data.text.str.contains('здравствуйте')])

#Вывод реплик,где менеджер представил себя
print(data.loc[data['role']=='manager'][data.text.str.contains('зовут')])

#Извлекать имя менеджера
print(data.loc[data['role']=='manager'][data.text.str.contains('ангелина')])


#Извлекать реплики,где менеджер попрощался - совмещаем два условия
#1 способ
print(data.loc[data['role']=='manager'][data.text.str.contains('до свидания')])

#2 способ
print(data[(data.text.str.contains('до свидания')) & (data.role=='manager')])

#Извлекать название компании

