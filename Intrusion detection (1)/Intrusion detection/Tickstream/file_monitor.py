from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import time

# Set up logging
logging.basicConfig(filename='file_monitor.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class FileChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("AAPL.csv"):
            logging.info(f"{event.src_path} has been modified.")

if __name__ == "__main__":
    path_to_watch = '.'  # Monitor current directory, or specify the path where 'AAPL.csv' is located
    event_handler = FileChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path_to_watch, recursive=False)
    observer.start()

    print("Monitoring file changes. Press Ctrl+C to stop.")
    
    try:
        while True:
            time.sleep(1)  # Sleep for a while to reduce CPU usage
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
