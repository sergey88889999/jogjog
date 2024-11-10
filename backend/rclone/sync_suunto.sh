#!/bin/bash

# Путь к папке в Google Drive (относительный путь)
SOURCE="gdrive:suunto-trainings"

# Путь в контейнере
DESTINATION="/app/suunto-trainings"

# Создаём лог-файл
LOG_FILE="/app/logs/sync_suunto_$(date +%Y%m%d).log"

# Выполняем синхронизацию
echo "Начало синхронизации: $(date)" >> "$LOG_FILE"

rclone sync "$SOURCE" "$DESTINATION" \
    --progress \
    --log-file="$LOG_FILE" \
    --log-level INFO \
    --transfers 4 \
    --checkers 8 \
    --drive-acknowledge-abuse \
    --filter-from "/app/scripts/rclone-filters.txt"

echo "Синхронизация завершена: $(date)" >> "$LOG_FILE"
