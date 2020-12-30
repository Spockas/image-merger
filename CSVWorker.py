import queue
import time

import ExcelEditor
import CsvToXlsx


class CSVWorker:
    def __init__(self):
        ExcelEditor.init_excel()
        self.job_queue = queue.Queue()
        self.run = True
        self.convert = False

    def add_job(self, **kwargs) -> None:
        self.job_queue.put(kwargs)

    def job_count(self) -> int:
        return self.job_queue.qsize()

    def main_loop(self):
        print("CSVWorker has been started")
        sleepy = False
        while self.run:
            if not self.job_queue.empty():
                if sleepy:
                    print("There is something todo!")
                    sleepy = False
                parameters = self.job_queue.get()
                print("Writing:", parameters['seller_sku'])
                ExcelEditor.add_to_excel(**parameters)
                if self.convert:
                    print("Converting to xlsx")
                    CsvToXlsx.convert_all()
                    self.convert = False

            else:
                # wait for some jobs to be added
                if self.convert:
                    print("Converting to xlsx")
                    CsvToXlsx.convert_all()
                    self.convert = False
                if not sleepy:
                    print("Nothing for csv worker todo, going to sleep...")
                    sleepy = True
                time.sleep(5.)
