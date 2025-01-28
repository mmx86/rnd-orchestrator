import time
import subprocess
import watchdog.observers
import watchdog.events


class RestartHandler(watchdog.events.FileSystemEventHandler):
    def __init__(self, command):
        self.command = command  # Команда для запуска воркера
        self.process = None     # Процесс воркера
        self.start_process()    # Запуск воркера при инициализации

    def start_process(self):
        """
        Запускает процесс воркера.
        Если процесс уже запущен, он завершается перед перезапуском.
        """
        if self.process:
            print("Watchdog: Остановка текущего процесса...")
            self.process.terminate()  # Завершаем текущий процесс
            self.process.wait()       # Ждем завершения
        print("Watchdog: Запуск нового процесса...")
        self.process = subprocess.Popen(self.command)  # Запускаем новый процесс

    def on_modified(self, event):
        """
        Обрабатывает событие изменения файла.
        Перезапускает процесс, если изменен Python-файл.
        """
        if event.src_path.endswith('.py'):  # Проверяем, что изменен .py файл
            print(f"Watchdog: Обнаружено изменение в файле: {event.src_path}")
            self.start_process()  # Перезапускаем процесс


if __name__ == "__main__":
    # Команда для запуска воркера Temporal
    command = ['python', '-m', 'dsp_worker']  # Укажите путь к вашему worker.py

    # Создаем обработчик событий
    event_handler = RestartHandler(command)

    # Создаем наблюдатель и настраиваем его на отслеживание папки
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path='dsp_worker/', recursive=True)  # Мониторим папку с кодом

    # Запускаем наблюдатель
    observer.start()
    print("Watchdog: Автоматический перезапуск включен. Отслеживаются изменения в папке 'dsp_worker/'...")

    try:
        # Бесконечный цикл для поддержания работы скрипта
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # Останавливаем наблюдатель при нажатии Ctrl+C
        observer.stop()
        print("Watchdog: Остановка наблюдателя...")
    observer.join()
