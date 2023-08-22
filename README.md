# Об этом проекте
Перед нашей командой стояла задача в сжатые сроки создать веб-приложение в виде личного кабинета для систематизации всех процессов связанных с работой биолога вертикальных теплиц. Кейс компании "Иннофарм".
# Приложения к репозиторию
*Рекомендуемый порядок просмотра материалов указан ниже:*
1. [Презентация](https://github.com/Talich12/Innofarm/blob/main/%D0%9A%D0%B5%D0%B9%D1%81%20%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8%20%D0%98%D0%BD%D0%BD%D0%BE%D1%84%D0%B0%D1%80%D0%BC.pdf)
2. [Скринкаст (демо)](https://www.youtube.com/watch?v=SFrGbKufdbU)
3. [Figma](https://www.figma.com/file/B2w4PJ2iFjb5Xh1tZbbxxs/Untitled?type=design&node-id=0-1&t=2uNXsCrw0Qzxcprm-0)
4. [Экономический калькулятор](https://github.com/Talich12/Innofarm/blob/main/%D0%AD%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9%20%D0%BA%D0%B0%D0%BB%D1%8C%D0%BA%D1%83%D0%BB%D1%8F%D1%82%D0%BE%D1%80.xlsx)
5. [Экономическая составляющая проекта](https://github.com/Talich12/Innofarm/blob/main/%D0%92%D1%80%D0%B5%D0%BC%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5_%D0%B8_%D0%B4%D0%B5%D0%BD%D0%B5%D0%B6%D0%BD%D1%8B%D0%B5_%D0%B7%D0%B0%D1%82%D1%80%D0%B0%D1%82%D1%8B_%D0%BD%D0%B0_%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D1%83_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0.xlsx)
---
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

## Запуск backend

    ```bash
    python3 run.py
    ```

