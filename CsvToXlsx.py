import os
import glob
import csv
from xlsxwriter.workbook import Workbook


def covert_all():
    file_names = ["UK", "DE", "ES", "FR", "IT"]
    for filename in file_names:
        covert_one(filename)


def covert_one(filename):
    # noinspection PyBroadException
    try:
        for csvfile in glob.glob(os.path.join('.', filename + '.csv')):
            workbook = Workbook(csvfile[:-4] + '.xlsx')
            worksheet = workbook.add_worksheet()
            with open(csvfile, 'rt') as f:
                reader = csv.reader(f, delimiter=';')
                for r, row in enumerate(reader):
                    for c, col in enumerate(row):
                        worksheet.write(r, c, col)
            workbook.close()
    except:
        print("Failed to make file with " + filename)