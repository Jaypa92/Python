import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from plyer import notification

class Notification_Handler(FileSystemEventHandler):
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path
        self.notification_sent = False

    def on_modified(self, event):
        if event.src_path == self.file_path and not self.notification_sent:
            print("Sending notification...")
            try:
                notification.notify(
                    title="Important Update!",
                    message="Schedule has been updated!!"
                )
                print("Success!!")
                self.notification_sent = True
            except Exception as e:
                print(f"Failed to send notification: {e}")
        else:
            time.sleep(5)
            self.notification_sent = False

    def on_created(self, event):
        self.notification_sent = False

if __name__ == "__main__":
    path_to_watch = r"O:\SCHEDULES\magnetics\Magnetic Slitter Schedule 1 .xlsx"
    print(f"Watching file: {path_to_watch}")
    directory = os.path.dirname(os.path.abspath(path_to_watch))
    event_handler = Notification_Handler(path_to_watch)
    observer = Observer()
    observer.schedule(event_handler, directory, recursive=False)

    observer.start()
    print("Observer started")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        print("Observer stopped")

    observer.join()