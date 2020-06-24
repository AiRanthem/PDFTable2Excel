import logging
import os
import re

import pdfplumber

from PDFExtractor.BaseExtractor import BaseExtractor
from PDFExtractor.config import *

"""
ExtractorDirector

This class is a builder to build the data construction needed to generate an xslx file
It provides the data construction as shown below:

[
    [ table1.1, table1.2, table1.3 ],
    [ table2.1, table2.2],
    ...(for all pdf files)
]

table object is like below:
{
    "title": 标题
    "order": "序号",
    "id": "编号",
    "name": "名称",
    "institution": "单位",
    "principal": "负责人",
    "founds": "经费",
    "period": "实施周期"
}
"""


class ExtractorDirector:
    def __init__(self, file_dir: str):
        self.dir = file_dir
        self.files = list(map(lambda x: os.path.join(os.path.abspath(file_dir), x), os.listdir(file_dir)))
        self.pdfs = [pdfplumber.open(file) for file in self.files]
        self.extractors = [BaseExtractor(x,
                                         title_trigger_words=TITLE_TRIGGER_WORDS,
                                         title_keyword=TITLE_KEY_WORD,
                                         field_keywords=FIELD_KEY_WORDS)
                           for x in self.pdfs]

    def extract(self):
        """
        extract all table information from all pdf files via a couple of BaseExtractor

        :return: list of tables
        """
        print("开始解析数据")
        ret = []
        for i, e in enumerate(self.extractors):
            titles = e.parse_title()
            tables = e.parse_table()
            if tables:
                for j, table in enumerate(tables):
                    table["title"] = titles[j]
                    match = re.search(r"“(.*)”", titles[j])
                    if match:
                        table["project"] = match.group(1)
                ret.append(tables)
            else:
                logging.warning("文件解析失败(表格无法读取):\n{}".format(self.files[i]))
            # verify table rows
            for table in tables:
                all_orders = sorted(list(map(int, table["order"])))
                for j in range(1, all_orders[-1] + 1):
                    if j not in all_orders:
                        logging.warning("表格行解析失败(可能是由于改行格式特殊或不封闭等):\nline [{}] of table [{}]\nin file [{}]"
                                        .format(j, table["title"], self.files[i]))
        print("所有PDF表格均解析完毕")
        return ret
