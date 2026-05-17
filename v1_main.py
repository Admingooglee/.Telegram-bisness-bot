"""
Главный орхестратор автоматизации.
Загружает конфиг, запускает workers, координирует задачи.
"""
import asyncio
import json
from pathlib import Path
from loguru import logger
from typing import List, Dict

# Импорты из приложения
from apps.api.app.core.config import settings
from apps.api.app.services.orchestrator import Orchestrator
from apps.api.app.telegram.brain import Brain

logger.add("logs/main.log", rotation="500 MB", retention="7 days")

class MainApp:
    def __init__(self):
        self.settings = settings
        self.brain = Brain()
        self.orchestrator = Orchestrator()
    
    async def run(self):
        """Главный цикл приложения."""
        logger.info("🧠 Brain启动...")
        try:
            await self.orchestrator.run(self.brain)
        except Exception as e:
            logger.error(f"Fatal error: {e}")
            raise

if __name__ == "__main__":
    app = MainApp()
    asyncio.run(app.run())