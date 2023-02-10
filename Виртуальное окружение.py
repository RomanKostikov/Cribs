python -m venv new_venv # - создать виртуальное окружение
# source venv/bin/activate - активация ВО для линукс
venv\Scripts\activate # - активация в виндоус (обязательно \ - обратный слэш)
deactivate # - деактивация виртуального окружения
pip freeze # - распечатает установленные пакеты(библиотеки) (создаёт файл зависимостей)
pip install -U pip setuptools # - U-сокращенно upgrade, далее следуют имя или имена модулей, которые требуется обновить,
# в данном случае setuptools
python.exe -m pip install -U pip setuptools #- тоже самое
pip install requests lxml # - установка библиотек requests и lxml - если нужно установить несколько библиотек,
# то можно перечислить их через пробел
pip uninstall lxml -y # - удаление библиотеки, в данном случае lxml
pip uninstall -y -r requirements.txt # - удаляет все библиотеки, которые были прописаны в файле requirements.txt
pip freeze > requirements.txt # - создаёт файл с зависимостями (в нём прописываются все библиотеки и версии нашего проекта)
pip install -r requirements.txt # - устанавливаем все библиотеки с зависимостями

cd # - перейти в нужную папку
cd.. # - на уровень выше

Что делать если pycharm не видит библиотеку
https://www.youtube.com/watch?v=3SvmrzqVmXo
https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#existing-environment
