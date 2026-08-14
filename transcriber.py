"""Whisper Transcriber — локальная транскрибация аудио в текст."""

from faster_whisper import WhisperModel
import time

# Настройки
MODEL_SIZE = "medium"      # tiny, small, medium, large-v3
DEVICE = "cuda"            # cuda или cpu
COMPUTE_TYPE = "int8"      # int8 или float32
INPUT_FILE = "test.wav"
OUTPUT_FILE = "transcript.txt"

print(f"Загрузка модели {MODEL_SIZE}...")
start = time.time()

model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)
print(f"Модель загружена за {time.time() - start:.1f} сек")

print("Распознавание...")
segments, info = model.transcribe(
    INPUT_FILE,
    language="ru",
    vad_filter=True,
    beam_size=5
)

print(f"Язык: {info.language} ({info.language_probability:.1%})")
print("=" * 50)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for seg in segments:
        mins, secs = divmod(int(seg.start), 60)
        line = f"[{mins:02d}:{secs:02d}] {seg.text.strip()}"
        print(line)
        f.write(line + "\n")

print("=" * 50)
print(f"Готово за {time.time() - start:.1f} сек")
print(f"Результат: {OUTPUT_FILE}")
