# Whisper Transcriber

Локальная транскрибация аудио в текст с таймкодами.

## Возможности
- Распознавание русской речи через Faster-Whisper
- VAD-фильтр — автоматически убирает тишину
- Таймкоды для каждого сегмента
- Работает на GPU (CUDA) и CPU

## Установка

pip install -r requirements.txt

## Использование

Положите аудиофайл `test.wav` рядом со скриптом.

python transcriber.py

Результат — `transcript.txt`.

## Модель
- По умолчанию: medium (int8)
- Для слабого ПК: small или tiny
- Для сервера с GPU: large-v3 (float32)

## Автор
[Твоё имя] — веб-разработчик, Telegram-боты, нейронки
GitHub: @[твой_username]
