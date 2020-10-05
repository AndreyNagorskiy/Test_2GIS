# установка базового образа
FROM python:3.8

# копирование файла зависимостей
COPY requirements.txt .

COPY ["main.py", "small_memory_test.xml","big_memory_test.xml", "middle_memory_test.xml", "./" ]

# установка зависимостей
RUN pip install -r requirements.txt

# команда, выполняемая при запуске контейнера
CMD [ "python", "main.py" ]