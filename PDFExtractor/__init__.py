from PDFExtractor.ExtractorDirector import ExtractorDirector
from PDFExtractor.ExcelGenerator import ExcelGenerator

import datetime
def pdf2excel(input_dir: str, output_dir: str, output_filename: str = None):
    """
    解析一组PDF文件并生成Excel表格

    :param input_dir: PDF文件的目录. 请在该目录下放置所有的待处理PDF文件
    :param output_dir: Excel表格输出目录,生成的文件会输出到这里
    :param output_filename: 输出文件的文件名. 缺省为日期
    """
    if output_filename is None:
        output_filename = str(datetime.date.today())
    director = ExtractorDirector(input_dir)
    info = director.extract()
    generator = ExcelGenerator(output_dir, output_filename, info)
    generator.process()
    generator.save()
