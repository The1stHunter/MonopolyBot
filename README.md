# MonopolyBot
## Что он делает?
Данный бот создан для создания более честного рандома при игре 
в дорожную версию монополии. Если вы попали на поле "Общественная казна"
или "Шанс", напишите боту, и он скажет, что вам делать.
## Как он работает?
Перед запуском бота создаётся хранилище со всеми вариантами действий.
При общении с ботом используется кастомная клавиатура,
при использовании которой, бот в ответ присылает рандомный вариант
действия, взятый из хранилища.
## Какие файлы для чего нужны?
* main.py - основной код бота
* utils.py - вспомогательные функции для бота
* config.example.py - пример файла конфигурации, чтобы сделать
его рабочим, уберите из названия .example, в переменную *TOKEN*
запишите токен, присланый *BotFather*, в переменную *storage* 
имя файла хранилища
* requirements.txt - список всех используемфх библиотек
