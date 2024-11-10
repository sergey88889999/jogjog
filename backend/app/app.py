import time
import sys
import signal
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import socket

# Загрузка переменных из .env файла
load_dotenv()

def connect_to_database():
    try:   
        # Вывод IP-адреса для отладки
        ip_address = socket.gethostbyname(os.getenv("DB_HOST"))
        print(f"Подключение к базе данных по адресу: {ip_address}")
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        if connection.is_connected():
            print("База данных ОК!")
            return connection
    except Error as e:
        print(f"Ошибка при подключении к MySQL: {e}")
        return None

def signal_handler(sig, frame):
    print("Получен сигнал завершения. Завершаем работу...")
    sys.exit(0)

def main():
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    print("Ждем 10 секунд для запуска всех сервисов...")
    time.sleep(10)
    
    connection = connect_to_database()
    if not connection:
        print("Не удалось подключиться к базе данных. Завершаем работу.")
        sys.exit(1)

    print("Бэкенд-сервер запущен и ожидает команд...")
    while True:
        time.sleep(10)  # Просто ждем, имитируя работу
        print("Сервер работает...")

if __name__ == "__main__":
    main()