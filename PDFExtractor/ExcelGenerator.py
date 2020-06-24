import os

import xlwt

from PDFExtractor.config import *

"""
ExcelGenerator

This class takes information extracted from all PDF files and generate a Excel table
"""


class ExcelGenerator:
    def __init__(self, output_dir: str, output_file: str, info: list):
        self.output_dir = output_dir
        self.output_file = output_file
        self.info = info  # information from PDF
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workbook.add_sheet(output_file)
        self.init_work_book()

    def init_work_book(self):
        for i, head in enumerate(WORKBOOK_HEAD):
            self.sheet.write(0, i, head)

    def save(self):
        path = os.path.abspath(os.path.join(self.output_dir, self.output_file + ".xls"))
        self.workbook.save(path)
        print("文件保存成功: {}".format(path))

    def process(self):
        # i = which row
        i = 1
        for file in self.info:
            for table in file:
                # row is the row number in the table
                for row in range(len(table['order'])):
                    # write a row. j = which column
                    for j, field in enumerate(WORKBOOK_FIELD):
                        try:
                            if field == "title" or field == "project":
                                content = table[field]
                            else:
                                content = table[field][row]
                            self.sheet.write(i, j, content)
                        except:
                            pass
                    i += 1


