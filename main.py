import lxml.etree as ET
from datetime import datetime, date, timedelta
from memory_profiler import profile


XML_FILE_PATH = 'big_memory_test.xml'


# @profile
def handle_input(count):
    if count == 1:
            get_data(XML_FILE_PATH)
    if count == 2:
        employees = []
        count = 1
        input_count_employees = int(input('Введите количество сотрудников: '))
        while count <= input_count_employees:
            employee = str(input(f'Введите имя {count}-ого сотрудника: '))
            employees.append(employee)
            count += 1
        get_data_by_names(XML_FILE_PATH, employees)
    if count == 3:
        input_start_time = (str(input('Введите дату начала интервала в формате дд-мм-гггг: ')))
        start_time = datetime.strptime(input_start_time, r"%d-%m-%Y")
        truncated_start_time = date(start_time.year, start_time.month, start_time.day)
        input_end_time = (str(input('Введите дату конца интервала в формате дд-мм-гггг: ')))
        end_time = datetime.strptime(input_end_time, r"%d-%m-%Y")
        truncated_end_time = date(end_time.year, end_time.month, end_time.day)
        get_data_by_date(XML_FILE_PATH, start_time, end_time,truncated_start_time, truncated_end_time)
    if count == 4:
        employees = []
        count = 1
        input_count_employees = int(input('Введите количество сотрудников: '))
        while count <= input_count_employees:
            employee = str(input(f'Введите имя {count}-ого сотрудника: '))
            employees.append(employee)
            count += 1
        input_start_time = (str(input('Введите дату начала интервала в формате дд-мм-гггг: ')))
        start_time = datetime.strptime(input_start_time, r"%d-%m-%Y")
        truncated_start_time = date(start_time.year, start_time.month, start_time.day)
        input_end_time = (str(input('Введите дату конца интервала в формате дд-мм-гггг: ')))
        end_time = datetime.strptime(input_end_time, r"%d-%m-%Y")
        truncated_end_time = date(end_time.year, end_time.month, end_time.day)
        get_data_by_date_and_names(XML_FILE_PATH, start_time, end_time, employees,truncated_start_time, truncated_end_time)

# @profile
def get_data(file_path):
    sum_seconds = 0
    for event, elem in ET.iterparse(file_path, events=('end',), tag='person'):
        start_datetime = (list(elem)[0]).text
        end_datetime = (list(elem)[1]).text
        seconds = (datetime.strptime(end_datetime, r"%d-%m-%Y %H:%M:%S") - datetime.strptime(start_datetime, r"%d-%m-%Y %H:%M:%S")).seconds
        sum_seconds += seconds
        if elem.getprevious() is not None:
            del elem.getparent()[0]
    convert_time(sum_seconds)


# @profile
def get_data_by_names(file_path, names):
    sum_seconds = 0
    for event, elem in ET.iterparse(file_path, events=('end',), tag='person'):
        for name in names:
            if elem.attrib['full_name'] == name:
                start_datetime = (list(elem)[0]).text
                end_datetime = (list(elem)[1]).text
                seconds = (datetime.strptime(end_datetime, r"%d-%m-%Y %H:%M:%S") - datetime.strptime(start_datetime, r"%d-%m-%Y %H:%M:%S")).seconds
                sum_seconds += seconds
        if elem.getprevious() is not None:
            del elem.getparent()[0]

    convert_time(sum_seconds)

# @profile
def get_data_by_date(file_path, start_time, end_time, truncated_start_time, truncated_end_time):
    sum_seconds = 0
    for event, elem in ET.iterparse(file_path, events=('end',), tag='person'):
        sum_seconds += check_data(elem,truncated_start_time, truncated_end_time)

        if elem.getprevious() is not None:
            del elem.getparent()[0]
    
    if sum_seconds > 0:
        convert_time(sum_seconds)
    else:
        print('За этот интервал не найдено информации')


# @profile
def get_data_by_date_and_names(file_path, start_time, end_time, names,truncated_start_time, truncated_end_time):
    sum_seconds = 0
    for event, elem in ET.iterparse(file_path, events=('end',), tag='person'):
        for name in names:
            if elem.attrib['full_name'] == name:
                sum_seconds += check_data(elem,truncated_start_time, truncated_end_time) 
        if elem.getprevious() is not None:
            del elem.getparent()[1]  
    if sum_seconds > 0:
        convert_time(sum_seconds)
    else:
        print('За этот интервал не найдено информации')


def check_data(elem,truncated_start_time, truncated_end_time):
    start_datetime = datetime.strptime((list(elem)[0]).text, r"%d-%m-%Y %H:%M:%S")
    truncated_start_datetime = date(start_datetime.year, start_datetime.month, start_datetime.day)
    end_datetime = datetime.strptime((list(elem)[1]).text, r"%d-%m-%Y %H:%M:%S")
    truncated_end_datetime = date(end_datetime.year, end_datetime.month, end_datetime.day)
    if truncated_start_datetime >= truncated_start_time and truncated_end_datetime <= truncated_end_time:
        seconds =  (end_datetime - start_datetime).seconds
        return seconds
    else:
        return 0       


def convert_time(seconds):
    h=seconds/3600 
    m=seconds%3600/60
    s=seconds%3600%60
    if int(h) == 1:
        hours = 'час'
    elif int(h) > 1 and int(h) < 5:
        hours = 'часа'
    else:
        hours = 'часов'

    print(f'{int(h)} {hours} {int(m)} минут {int(s)} секунд')


if __name__ == "__main__":
    print('В этом скрипте есть следующие возможности:')
    print('1 - общее время всех сотрудников(без фильтров);')
    print('2 - фильтр по сотрудникам;')
    print('3 - фильтр по интервалу дат;')
    print('4 - фильтр по сотрудникам и интервалу дат;')

    count = int(input('Выберите фильтр: '))
    handle_input(count)