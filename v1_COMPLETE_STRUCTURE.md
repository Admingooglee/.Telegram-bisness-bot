# GiftTelegramRever - Complete Project Structure

## Architecture Overview

### Repositories (Data Access Layer)
- `app/repositories/base.py` - Generic repository pattern
- `app/repositories/user_repository.py` - User data access
- `app/repositories/wallet_repository.py` - Wallet operations
- `app/repositories/transfer_repository.py` - Transfer history
- `app/repositories/gift_repository.py` - Gift management
- `app/repositories/notification_repository.py` - Notifications

### Services (Business Logic Layer)
- `app/services/user_service.py` - User management
- `app/services/auth_service.py` - Authentication flow
- `app/services/wallet_service.py` - Wallet operations
- `app/services/transfer_service.py` - Transfer processing
- `app/services/gift_service.py` - Gift logic
- `app/services/telegram_service.py` - Telegram API integration
- `app/services/notification_service.py` - Notifications

### API Routes
- `app/api/routes/auth.py` - Auth endpoints
- `app/api/routes/users.py` - User endpoints
- `app/api/routes/wallets.py` - Wallet endpoints
- `app/api/routes/transfers.py` - Transfer endpoints
- `app/api/routes/gifts.py` - Gift endpoints
- `app/api/routes/admin.py` - Admin panel

### Telegram Bot (aiogram)
- `app/telegram/handlers/start.py` - /start command
- `app/telegram/handlers/menu.py` - Menu handlers
- `app/telegram/handlers/business.py` - Business handlers
- `app/telegram/handlers/transfers.py` - Transfer handlers
- `app/telegram/handlers/gifts.py` - Gift handlers
- `app/telegram/middlewares/auth.py` - Auth middleware
- `app/telegram/keyboards/reply.py` - Reply keyboards
- `app/telegram/keyboards/inline.py` - Inline keyboards
- `app/telegram/services/` - Bot services
- `app/telegram/states/` - FSM states

### Frontend Structure (Next.js)