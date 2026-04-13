# Cat Facts Collector

Скрипт на Python, который получает случайный факт о кошках из публичного API и сохраняет его в текстовый файл. При каждом запуске добавляет новый факт, не затирая предыдущие.

## Возможности

- Получает случайный факт с [catfact.ninja](https://catfact.ninja)
- Сохраняет факты в `facts.txt`, каждый с новой строки
- При повторных запусках дополняет файл, не удаляя старые записи
- Корректно обрабатывает недоступность API

## Требования

- Python 3.x
- Стандартная библиотека (сторонние зависимости не нужны)

## Установка

```bash
git clone https://github.com/Pavel-qr/MEDODS.git
cd MEDODS
```

## Использование

```bash
python3 cat_facts.py
```

Пример вывода:

```
Факт сохранён: A cat's nose is as unique as a human's fingerprint.
```

После нескольких запусков `facts.txt` будет выглядеть так:

```
A cat's nose is as unique as a human's fingerprint.
Cats take between 20-40 breaths per minute.
Cats have 230 bones, while humans only have 206.
```

## Обработка ошибок

Если API недоступен, скрипт выведет сообщение и завершится без исключения:

```
Не удалось получить факт
```

## API

Используется публичный бесплатный API [catfact.ninja](https://catfact.ninja) — регистрация и ключи не требуются.

Пример ответа:

```json
{
  "fact": "Cats sleep 70% of their lives.",
  "length": 30
}
```

## Структура проекта

```
cat-facts-collector/
├── cat_facts.py   # основной скрипт
├── facts.txt      # файл с накопленными фактами (создаётся автоматически)
└── README.md
```

## Лицензия

MIT
