#!/bin/bash

# Запуск cron демона
cron

# Первичная синхронизация при старте
/app/scripts/sync_suunto.sh

# Запуск основного приложения
exec python app/app.py