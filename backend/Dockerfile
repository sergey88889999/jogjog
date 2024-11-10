FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

# Установка необходимых зависимостей
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Установка rclone
RUN curl https://rclone.org/install.sh | bash

# Создание директории для конфигурации rclone
RUN mkdir -p /root/.config/rclone

# ENV PATH="/root/.local/bin:$PATH"

RUN rclone --version

# Копирование конфигурации rclone и скриптов
COPY ./rclone/rclone.conf /root/.config/rclone/
COPY ./rclone/sync_suunto.sh /app/scripts/
COPY ./rclone/rclone-filters.txt /app/scripts/

# Установка прав на выполнение скрипта
RUN chmod +x /app/scripts/sync_suunto.sh

# Установка cron
RUN apt-get update && apt-get install -y cron

# Добавление задачи в cron
RUN echo "*/30 * * * * /app/scripts/sync_suunto.sh >> /var/log/cron.log 2>&1" > /etc/cron.d/sync-cron
RUN chmod 0644 /etc/cron.d/sync-cron
RUN crontab /etc/cron.d/sync-cron

# Создание файла для логов
RUN touch /var/log/cron.log

# Скрипт запуска
COPY ./rclone/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]



# CMD ["python", "app/app.py"]
