# -*- coding: utf-8 -*-
import requests
from tqdm import tqdm
import os
import threading

class downloader(threading.Thread):
    '''
    downloader class
        args:
        thread: int, the number of threads
        pagelist: list, the list of the urls
        TempPath(optional): str, the path of the temp folder
    Use:
        downloader_instance = downloader(thread_count, pagelist)
        downloader_instance.start()
        downloader_instance.join()
    '''
    def __init__(self, pagelist, TempPath, thread = 10):
        super().__init__()
        self.__thread = int(thread)
        self.__pagelist = pagelist
        self.TEMP_PATH = TempPath
        self.progress_lock = threading.Lock()
        if not os.path.exists(self.TEMP_PATH):
            os.makedirs(self.TEMP_PATH)

    def download_image(self, url, filename, progress_bar):
        response = requests.get(url)
        with open(filename, 'wb') as f:
            f.write(response.content)
        with self.progress_lock:
            progress_bar.update(1)

    def run(self):
        progress_bar = tqdm(total=len(self.__pagelist), desc="Downloading")
        threads = []
        for index, url in enumerate(self.__pagelist):
            filename = os.path.join(self.TEMP_PATH, "{:03}.jpg".format(index))
            while threading.active_count() > self.__thread:
                continue
            thread = threading.Thread(target=self.download_image, args=(url, filename, progress_bar))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        progress_bar.close()
        tqdm.write("Download completed!")