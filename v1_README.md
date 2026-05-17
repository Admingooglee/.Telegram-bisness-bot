# 🧠 Brain - Автоматизация Telegram & Gmail

Мультипоточный оркестратор для автоматизации Telegram и Google аккаунтов с поддержкой прокси.

## 📋 Структура проекта

```
apps/api/app/
├── api/              # FastAPI маршруты
├── auth/             # Управление аутентификацией
├── core/             # Конфиг, прокси-менеджер
├── db/               # БД
├── models/           # SQLAlchemy модели
├── schemas/          # Pydantic схемы
├── repositories/     # Доступ к данным
├── services/         # Бизнес-логика
├── workers/          # Воркеры для задач
├── telegram/         # Telegram Brain
├── events/           # События и обработчики
├── middleware/       # Middleware
├── permissions/      # Контроль доступа
├── notifications/    # Уведомления
├── queues/           # Очереди задач
└── websocket/        # WebSocket
```

## 🚀 Быстрый старт

```bash
# Установка
pip install -r requirements.txt

# Переменные окружения
cp .env.example .env
# Заполнить .env

# Запуск
python main.py
```

## 📦 Требования

- Python 3.10+
- FastAPI
- Telethon
- aiohttp
- loguru

## 📝 Лицензия

MIT