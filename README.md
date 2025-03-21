### **Telegram-бот для парсинга сайтов**

---

## **Установка**

1. **Склонируйте репозиторий**:
   ```bash
   git clone https://github.com/MaskedGod/technesisl_parse_bot
   ```

2. **Установите зависимости**:
   ```bash
   uv pip install --lockfile uv.lock
   ```

3. **Создайте файл `.env` с токеном вашего бота**:
   ```env
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   ```

4. **Запустите бота**:
   ```bash
   python main.py
   ```

---

## Использование

После запуска бота вам будут доступны следующие действия через меню:

- **Загрузить файл**: отправьте Excel-файл с данными.  
  Файл должен содержать следующие столбцы:  
  - `title` — название товара,  
  - `url` — ссылка на сайт,  
  - `xpath` — путь к элементу с ценой.

- **Рассчитать средние цены**: выполните парсинг сайтов из базы данных.

- **Помощь**: получите информацию о командах.

Также вы можете использовать команды напрямую:
- `/start`: начать работу с ботом.
- `/parse`: рассчитать средние цены.
- `/help`: получить информацию о командах.

---

### Пример Excel-файла

| title       | url                          | xpath                  |
|-------------|------------------------------|------------------------|
| Зюзюблик 1  | https://example.com/product1 | //div[@class='price']  |
| Зюзюблик 2  | https://example.com/product2 | //span[@id='price']    |
| Зюзюблик 3  | https://example.com/product3 | //p[@class='price-tag']|
