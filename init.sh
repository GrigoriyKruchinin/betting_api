#!/bin/bash

set -e

echo -e "\n\n\nНачало начальной настройки...\n\n\n"

# Сборка и запуск контейнеров в фоновом режиме
echo -e "Сборка и запуск контейнеров...\n"
docker-compose up --build -d

# Применение миграций
echo -e "Применение миграций для сервиса bet-maker...\n"
docker-compose run bet-maker alembic upgrade head

# Запуск приложения в режиме foreground
echo -e "Начальная настройка завершена. Приложение запущено.\n"
docker-compose up

# Если приложение останавливается, выводим сообщение
echo -e "\n\n\nПриложение остановлено.\n\n\n"
