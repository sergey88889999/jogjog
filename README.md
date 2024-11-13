# jogjog - это пет-проект на python3

**Онлайн-тренер по бегу** - идея помочь себе в подготовке к беговым соревнованиям, таким как марафон и полумарафон. Анализ на основе данных из беговых часов Suunto.

## Технологии
Микросервисная архитектура:

- **Backend**: Python3
- **Frontend**: Nginx
- **База данных**: MySQL
- **Docker**: для контейнеризации и оркестрации всех сервисов


## Функциональность

#### Backend
- **Загрузка данных**: API Suunto не реализован(!) сохраниение беговых тренировок с часов Suunto в ручную. Реализовано как выгрузка тренировок из приложения Suunto с телефона в папку(suunto-trainings) на GoogleDrive, и автоматическая синхронизация c папкой(suunto-trainings) на сервере с помощью костыля - rclone. Далее парсинг fit - файлов и извлечение из них данных.
- **Статистика и анализ**: сбор и анализ данных о тренировках для отслеживания прогресса.
- **Персонализированное планирование тренировок**: генерация плана тренировок в зависимости от поставленных целей (например, подготовка к марафону или полумарафону).

#### База данных
- **Хранение данных**: Загрузка и хранение данных во внешней базе MySQL для дальнейшего использования.
  
#### Веб-морда
- **Веб-интерфейс**: доступный интерфейс для мониторинга статистики и управления планом тренировок.

---

## Установка

Перед установкой убедитесь, что у вас есть настроенный сервер на Debian 12 с настроенной сетью, файрволом, а также установленными Docker и Git. 

[Тут установка](doc/install-debian.md) для тестового сервера с Debian 12.


1. Склонируйте репозиторий:
    ```bash
    git clone https://github.com/sergey88889999/jogjog.git
    cd jogjog
    ```

2. Запустите контейнеры с помощью Docker Compose:
    ```bash
    docker-compose up -d
    ```