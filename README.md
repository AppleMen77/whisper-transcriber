# Whisper Transcriber

> Локальная транскрибация аудио в текст с таймкодами и VAD-фильтрацией

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/AppleMen77/whisper-transcriber?style=social)](https://github.com/AppleMen77/whisper-transcriber)

## Возможности

- Распознавание русской речи через Faster-Whisper
- VAD-фильтр — автоматическое удаление тишины
- Таймкоды для каждого сегмента
- Поддержка GPU (CUDA) и CPU
- Точная транскрибация с оптимизацией под русский язык
- Экспорт в текстовый файл

## Технологии

![Faster-Whisper](https://img.shields.io/badge/Faster--Whisper-Model-blue)
![PyTorch](https://img.shields.io/badge/PyTorch-Deep%20Learning-orange)
![VAD](https://img.shields.io/badge/VAD-Noise%20Filter-green)
![CUDA](https://img.shields.io/badge/CUDA-GPU%20Support-purple)

## Требования

- Python 3.8 или выше
- 4+ GB RAM (для medium модели)
- GPU с CUDA (опционально, для ускорения)

## Быстрый старт

### Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/AppleMen77/whisper-transcriber.git
cd whisper-transcriber

# Установите зависимости
pip install -r requirements.txt
```

### Использование

1. Положите аудиофайл `test.wav` в папку со скриптом
2. Запустите транскрибацию:

```bash
python transcriber.py имя_файла.wav
```

3. Результат будет сохранён в `transcript.txt`

### Формат вывода

```
[00:00:00] Привет! Это тестовое сообщение.
[00:00:03] Проверяем работу транскрибации.
...
```

## Конфигурация

### Выбор модели

В файле `transcriber.py` измените параметр `model_size`:

| Модель | Размер | Скорость | Качество | Требования |
|--------|--------|----------|----------|------------|
| `tiny` | ~75 MB | Очень быстро | Базовое | 1 GB RAM |
| `small` | ~450 MB | Быстро | Хорошее | 2 GB RAM |
| `medium` | ~1.5 GB | Средне | Высокое | 4 GB RAM |
| `large-v3` | ~3 GB | Медленно | Максимальное | 8 GB RAM + GPU |

```python
# Для слабого ПК
model = WhisperModel("small", device="cpu", compute_type="int8")

# Для обычного использования
model = WhisperModel("medium", device="auto", compute_type="int8")

# Для сервера с GPU (максимальное качество)
model = WhisperModel("large-v3", device="cuda", compute_type="float32")
```

### Настройка VAD-фильтра

```python
# Фильтрация тишины (по умолчанию включена)
vad_filter=True

# Минимальная длительность тишины для отсечения (в миллисекундах)
vad_parameters=dict(min_silence_duration_ms=500)
```

## Структура проекта

```
whisper-transcriber/
├── transcriber.py      # Основной скрипт
├── requirements.txt    # Зависимости
├── test.wav           # Входной аудиофайл
├── transcript.txt     # Результат транскрибации
└── README.md          # Документация
```

## Примеры использования

### Базовое использование

```python
from transcriber import transcribe_audio

# Транскрибация с настройками по умолчанию
transcribe_audio("test.wav", "transcript.txt")
```

### Расширенные настройки

```python
from transcriber import transcribe_audio

# С указанием модели и устройства
transcribe_audio(
    input_file="audio.wav",
    output_file="result.txt",
    model_size="large-v3",
    device="cuda",
    compute_type="float32"
)
```

## Производительность

Ориентировочное время обработки 1 часа аудио:

| Модель | CPU | GPU (CUDA) |
|--------|-----|------------|
| `tiny` | ~5 мин | ~1 мин |
| `small` | ~15 мин | ~3 мин |
| `medium` | ~40 мин | ~8 мин |
| `large-v3` | ~2 часа | ~20 мин |

## Решение проблем

### Ошибка "CUDA out of memory"

Уменьшите модель или используйте CPU:

```python
model = WhisperModel("small", device="cpu", compute_type="int8")
```

### Медленная обработка

Используйте int8 квантизацию и уменьшите модель:

```python
model = WhisperModel("small", device="auto", compute_type="int8")
```

### Плохое качество распознавания

- Используйте более крупную модель
- Убедитесь в хорошем качестве аудио
- Проверьте, что аудио в формате WAV с частотой 16kHz или выше

## Лицензия

MIT License. Свободное использование и модификация.

## Автор

AppleMen77 — веб-разработчик, Telegram-боты, нейронки

GitHub: [@AppleMen77](https://github.com/AppleMen77)

Telegram: [@wexiwy](https://t.me/wexiwy)
