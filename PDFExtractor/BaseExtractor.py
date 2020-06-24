import re

from PDFExtractor.utils import *

"""
BaseExtractor
@author: Airanthem at 2020
This class performs some basic extract operations on a PDF document.
To build a BaseExtractor, please offer a PDF object to it.
"""


class BaseExtractor:

    def __init__(self, pdf: pdfplumber.pdf.PDF, title_trigger_words: list, title_keyword: str, field_keywords: dict):
        """
        :param pdf: a PDF object
        :param title_trigger_words: if a string contains this word, it is a title.
        """
        self.pdf = pdf
        self.title_trigger_words = title_trigger_words
        self.title_keyword = title_keyword
        self.field_keywords = field_keywords

    def parse_title(self) -> list:
        """
        extract the title from the pdf object
        :return the title of its pdf file
        """
        scanning = False  # start of a title is found, this may be the second of later part of that.
        ret = []  # to return
        temp = []  # deal with mutiple line titles.
        for page in self.pdf.pages:
            text = page.extract_text()
            # it's possible that a blank page exists which will let text be None.
            if text is None:
                continue
            lines = text.split('\n')

            for line in lines:
                if self.__is_part_of_title(line):
                    # middle part of a title
                    if scanning:
                        temp.append(line)
                    # find a new title
                    else:
                        scanning = True
                        temp = [line]
                else:
                    # just find an entire title
                    if scanning:
                        scanning = False
                        ret.append("".join(temp))
        # remove wrong titles ( maybe trigger words occur at other part of the document )
        for title in ret:
            if self.title_keyword not in title:
                ret.remove(title)
        return ret

    def __is_part_of_title(self, line: str) -> bool:
        for word in self.title_trigger_words:
            if word in line:
                return True
        return False

    def parse_table(self) -> list:
        """
        data constructure of a table (dict)
        {
            "title" : 标题, (only this field is of type string, others are of type list)
            "order":  序号,
            "id":     项目编号,
            "name":   项目名称,
            "institution": 项目牵头单位,
            "principal":  项目负责人,
            "founds":  中央财政经费,
            "period":  项目实施周期
        }
        :return: list of tables
        """
        # the three variables below are the same meaning as self.parse_title
        # for multi-thread reasons, set them as local variables
        ret = []
        temp = []

        # the i th column is of field column_map[i]
        column_map = []
        # to store current table head
        table_head = []

        for page in self.pdf.pages:
            table = page.extract_table()
            if table is None:
                continue
            # extract a table into list of strings
            table = [[re.sub(r"\s", "", grid) for grid in row] for row in table]

            for row in table:
                # find a table head
                if self.field_keywords["order"] in row[0]:
                    table_head = row
                    continue
                # find a new table
                if int(row[0]) == 1:
                    # record the last table
                    if temp:
                        ret.append(temp)
                    # init temp table and column mapper
                    temp = get_empty_table()
                    column_map = []
                    # find the column mapper
                    for grid in table_head:
                        for key, value in self.field_keywords.items():
                            if value in grid:
                                column_map.append(key)
                # add a new row to current temp table
                for i, grid in enumerate(row):
                    temp[column_map[i]].append(grid)
        if temp:
            ret.append(temp)
        return ret
