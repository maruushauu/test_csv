<h2 align="center">Test_csv</h2>


**Ссылки**:
- [Telegram](https://t.me/mariishu)

### Описание проекта:
Парсинг csv-файла 


### Инструменты разработки

**Стек:**
- Python >= 3.9
- pandas
- jupyter notebook

## Разработка

##### 1) Сделать форк репозитория


##### 2) Создать виртуальное окружение

    python -m venv venv
    
##### 3) Активировать виртуальное окружение

##### 4) Установить необходимые библиотеки:

    pip install pandas
    pip install notebook


##### 5) С помощью библиотеки pandas можем работать с csv-файлами двумя способами: в консоле PaCharm или с помощью  jupyter notebook
    
##### 6) Создаем DataFrame с помощью библиотеки pandas и читаем файл test_data.csv

    import pandas as pd
    data = pd.read_csv("test_data.csv")

##### 7) Для выполнения задания в библиотеке pandas используем фильтры и сортировку по csv-файлу
    
##### 8) Извлекаем реплики с приветствием – где менеджер поздоровался

    print(data.loc[data['role']=='manager'][data.text.str.contains('здравствуйте')])

##### 9) Извлекаем реплики, где менеджер представил себя

    print(data.loc[data['role']=='manager'][data.text.str.contains('зовут')])

##### 10) Извлекаем имя менеджера

    print(data.loc[data['role']=='manager'][data.text.str.contains('ангелина')])
    print(data.loc[data['role']=='manager'][data.text.str.contains('максим')])

##### 11) Извлекаем реплики, где менеджер попрощался

    #1 способ
    print(data.loc[data['role']=='manager'][data.text.str.contains('до свидания')])

    #2 способ
    print(data[(data.text.str.contains('до свидания')) & (data.role=='manager')])

##### 12) Извлекаем название компании

    print(data.loc[data['role']=='manager'][data.text.str.contains('диджитал')])

##### 13) С помощью библиотеки jupiter notebook, присвоим номер диолога = значение индексу,теперь dlg_id- первый столбец с индексами 1-5 

    df = pd.read_csv('test_data.csv',   
                index_col='dlg_id')

##### 14) Выводим каждый диалог по номеру индекса

    df.loc[[1]]
    df.loc[[2]]
    df.loc[[3]]
    df.loc[[4]]
    df.loc[[5]]

##### 15) Проверяем условие приветсвия менеджера в каждом диалоге