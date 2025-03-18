# CarePrescriber

CarePrescriber — это веб-приложение, разработанное специально для доктора Айболита, чтобы упростить процесс выписки лекарств и помочь его пациентам — жителям леса своевременно принимать назначенные препараты. Приложение сочетает в себе простоту использования, функциональность и удобство, что делает его незаменимым инструментом для заботы о здоровье лесных обитателей.

## Основные функции

- Расчет времени приема лекарств на основе заданного интервала.
- Поддержка гибкого расписания (например, прием каждые 15 минут).
- Выравнивание времени приема по заданному интервалу (например, кратно 15 минутам).
- Простое и интуитивно понятное использование.
---
## Мысли по проекту

Пришлось углубиться в задание проекта и сделать его максимально простым и понятным. К сожалению это просто тестовое задание, но если углубиться можно сделать реальный проект. Например: реализовать регистрацию пользователей, работу через API. Подкрутить телеграм бота, который бы опрашивал каждые 15 мин. "/next_takings?user_id=", только уже не по страховому полису, а например по телеграм нику, после чего присылал уведомления с данными о необходимости выпить определенные лекарства. Особенно это бы помогло возрастным людям.

## Установка

1. Склонируйте репозиторий:
   ```
   git clone https://github.com/Namari39/CarePrescriber.git
   ```
2. Перейдите в папку проекта:
   ```
   cd CarePrescriber
   ```
3. Установите необходимые зависимости:
   ```
   pip install -r requirements.txt
   ```
4. Сделайте миграции:
   ```
   python manage.py migrate
   ```
5. Загрузите фикстуры:
   ```
   python manage.py loaddata fixtures.json
   ```
  ---
## Использование

1. Запустите приложение:
   ```
   python manage.py runserver
   ```
2. Введите параметры расписания:
   - Откройте браузер на вкладке "http://127.0.0.1:8000/" (при стандартных настройках).
   - Перейдите во вкладку "Создать расписание".
   - Заполните форму.
   - Вернитесь на главную страницу.
3. Приложение рассчитает и выведет время приема лекарств.

## Зависимости

- Python 3.8 или выше.
- Установленные зависимости из `requirements.txt`.

---

## Автор

- Князев Денис **(Namari39)** - [GitHub](https://github.com/Namari39)
