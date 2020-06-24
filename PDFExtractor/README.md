# PDF2Excel解析器
## 环境配置
```powershell
pip install pdfplumber
pip install xlwt
```

## 使用说明与示例
1. 将要解析的一组PDF文件放在一个目录下(示例假设是"./inputs")
2. 建立一个输出excel文件的目录(也可以是现有的,示例假设为"./output")
3. 把这个包放在你的项目里，然后参照下面的例子使用：
```python
from PDFExtractor import pdf2excel

pdf2excel("./inputs", "./output", "name_it")
```

## 函数定义
```python
def pdf2excel(input_dir: str, output_dir: str, output_filename: str = None):
    """
    解析一组PDF文件并生成Excel表格

    :param input_dir: PDF文件的目录. 请在该目录下放置所有的待处理PDF文件
    :param output_dir: Excel表格输出目录,生成的文件会输出到这里
    :param output_filename: 输出文件的文件名. 缺省为日期
    """
```

## 注意点
+ input_dir务必保证其中所有的文件都是想要解析的PDF文档。否则会报错。
+ 现在的工具链只能解析标准的封闭式表格，可能会漏掉几行，注意看输出的WARNING。
+ 如果出现一个文件都解析失败的warning，那有可能是图片或其他形式的PDF，现在的工具没有办法解析，实在需要的话再去学习新的技术做添加。

## 自定义
### 全局参数
由于手里只有那么几个PDF文件，有可能出现我整理的模式不匹配的情况（比如不应该是title的被解析成了title）

也有可能excel的字段和需求不匹配（这个可能不算大）

如果出现类似的**内容性**问题，请去[config.py文件](config.py)中修改对应的参数即可。

### 代码修改
如果当前的代码不符合要求，请阅读对应的文件进行修改。
>每个文件中我都做了文档级的注释，请仔细阅读

文件说明
1. config.py：参数配置文件
2. init文件：定义了`pdf2excel`函数。不建议在这个函数中添加任何逻辑，所有工作请在对应的类中完成。
3. ExtractorDirector.py：采用Builder模式的导演类，负责构造PDF文档内容信息的数据结构。导演类建议单实例。
4. BaseExtractor.py：解析器，这个类负责解析PDF文件。注意：一个实例仅解析一个文件。解析器线程安全。
5. ExcelGenerator.py：生成Excel的工具类。如果要使用xlsx格式，需要用新的库并且重写这个类，很麻烦。
