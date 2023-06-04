# Об этом проекте
Перед нашей командой стояла задача в сжатые сроки создать веб-приложение в виде личного кабинета для систематизации всех процессов связанных с работой биолога вертикальных теплиц. Кейс компании "Иннофарм".
# Приложения к репозиторию
*Рекомендуемый порядок просмотра материалов указан ниже:*
1. Презентация
2. Скринкаст (демо)
3. [Figma](https://www.figma.com/file/B2w4PJ2iFjb5Xh1tZbbxxs/Untitled?type=design&node-id=0-1&t=2uNXsCrw0Qzxcprm-0)
4. Отдельные скриншоты дополненные комментариями (в случае если пересматривать демо ради конкретных моментов неудобно)
![innofarm](https://github.com/Talich12/Innofarm/blob/main/client/src/assets/images/logo.png)
---
## Инициализация backend-а
1. Установка venv
/root
    ```bash
    python3 -m venv venv
    ```
    ```bash
    source venv/bin/activate
    ```
2. Установка модулей
    ```bash
    pip install flask flask_sqlalchemy flask_cors flask_jwt_extended flask_migrate flask_marshmallow marshmallow_sqlalchemy Werkzeug
    ```
3. Инициализация базы данных
    ```bash
    flask db init
    ```
    ```bash
    flask db migrate -m "add_tables"
    ```
    ```bash
    flask db upgrade
    ```

## Запуск backend-а

    ```bash
    python3 run.py
    ```

