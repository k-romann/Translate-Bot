<h1>Создаем телеграм бот который должен принимать ФИО в кириллице и отдавать ФИО на латинице в соответствии с Приказом МИД России от 12.02.2020 № 2113.<h1>
Установить на компьютер Docker.
После того, как бот будет написал, нужно создать новый docker: - sudo docker build .
Далее необходимо проверить что новый образ действительно создан: - sudo docker images
Копируем IMAGE ID и вставляем вконце команды -sudo docker run -d -p 80:80 (IMAGE ID)
Проверяем, работает ли docker - sudo docker ps
ЕСли нужно остановить docker копирует CONTEINER ID и вставляем вконце команды - sudo docker stop (CONTEINER ID) 
