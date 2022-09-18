Django установленный системой автоматической установки cms LTD BEGET

=> Действия описанные ниже необходимо выполнять в docker-окружении выполнив команду ниже <=
$ ssh localhost -p222

для установки дополнительных модулей используйте pip
сам Django располагается в папке /home/d/davydoeh/davydoeh.beget.tech/public_html/venv/

для начала надо переключиться на текущий virtualenv
заходим в папку с проектом

$ cd /home/d/davydoeh/davydoeh.beget.tech/public_html
$ source venv/bin/activate

проверяем правильно ли определился путь до pip:
$ which pip
/home/d/davydoeh/davydoeh.beget.tech/public_html/venv/bin/pip

теперь мы можем пользоваться pip'ом для установки модулей не указывая полного пути до исполняемого файла:

$ pip install <Module-name>

где <Module-name> имя модуля который мы хотим установить

Для перезапуска passenger в папке проекта достаточно выполнить команду touch на пустом файле restart.txt

$ pwd
/home/d/davydoeh/davydoeh.beget.tech/public_html/HelloDjango/HelloDjango/tmp
$ touch restart.txt