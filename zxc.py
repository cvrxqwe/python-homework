from collections import deque
import time


# File Download Queue Class
class DownloadQueue:
    def __init__(self):
        # We use 'deque' (Double-Ended Queue) because it is much faster 
        # for removing elements from the beginning than a standard list.
        self.queue = deque()

    # 1. Accept file names and add them to the queue
    def add_file(self, filename):
        self.queue.append(filename)
        print(f"Added to queue: '{filename}'")

    # 2. Simulate downloading the next file and show remaining files
    def process_downloads(self):
        print("\n--- Starting Downloads ---")

        # The loop runs as long as the queue is not empty
        while self.queue:
            # .popleft() takes the FIRST element from the left side of the queue
            current_file = self.queue.popleft()

            print(f"Downloading: '{current_file}'...")

            # Simulate a small delay for realism (1 second)
            time.sleep(1)

            # The required output format
            print(f"Downloaded: '{current_file}'")

            # Show how many files are left
            remaining = len(self.queue)
            print(f"Files left in queue: {remaining}\n")

        # 3. Finish work when the queue is empty
        print("--- Queue is empty. All downloads finished. ---")


# Testing the System

downloader = DownloadQueue()

print("=== Adding Files ===")
downloader.add_file("report.pdf")
downloader.add_file("holiday_photos.zip")
downloader.add_file("setup.exe")
downloader.add_file("presentation.pptx")

# Start the automated downloading process
downloader.process_downloads()