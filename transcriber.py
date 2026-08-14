import os
import time
from faster_whisper import WhisperModel


# НАСТРОЙКИ


MODEL_SIZE = "medium"  # tiny, small, medium, large-v3
DEVICE = "cuda"        # cuda или cpu
COMPUTE_TYPE = "int8"  # int8 или float32
INPUT_FILE = "test.wav"
OUTPUT_FILE = "transcript.txt"


# ПРОВЕРКА ФАЙЛА


if not os.path.exists(INPUT_FILE):
    print(f"Ошибка: файл '{INPUT_FILE}' не найден.")
    print("Положите аудиофайл рядом со скриптом или укажите путь в INPUT_FILE.")
    exit(1)



# ЗАГРУЗКА МОДЕЛИ


print(f"Загрузка модели {MODEL_SIZE}...")
start_time = time.time()

model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)

print(f"Модель загружена за {time.time() - start_time:.1f} сек")


# РАСПОЗНАВАНИЕ


print("Распознавание...")

segments, info = model.transcribe(
    INPUT_FILE,
    language="ru",
    vad_filter=True,
    beam_size=5
)

print(f"Язык: {info.language} (вероятность {info.language_probability:.1%})")
print("=" * 50)


# СОХРАНЕНИЕ


with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for seg in segments:
        mins, secs = divmod(int(seg.start), 60)
        line = f"[{mins:02d}:{secs:02d}] {seg.text.strip()}"
        print(line)
        f.write(line + "\n")

print("=" * 50)
print(f"Готово за {time.time() - start_time:.1f} сек")
print(f"Результат: {OUTPUT_FILE}")