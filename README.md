## D5_10_Heroku

Действия в Git

$ git init

$ git add .

$ git commit -m "initial commit"

$ heroku create

$ heroku config:set DISABLE_COLLECTSTATIC=1 -- Для того чтобы небыло ошибки запрещаем на время установки обращение к статическим файлам


Правим модуль в Heroku

Resources => добавляем Heroku Postgres

Settings => Reveal Config Vars добавляем SECRET_KEY и его значение


$ git add .

$ git commit -m "about to deploy"

$ git push heroku master

После получения положительного результата о установке

$ heroku config:set DISABLE_COLLECTSTATIC=0 -- Подключаем статические файлы после установки приложения

$ heroku run python manage.py migrate

$ heroku run python manage.py loaddata data.xml


$ heroku run python manage.py createsuperuser
