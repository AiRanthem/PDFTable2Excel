# PDFTable2Excel
该项目主要作用是把一些公示PDF文件中的表格提取成xls表格。

（PDF公示和xls格式，十分古板的感觉hh）

## 适用范围
目前的实现适合类似 [inputs目录](inputs) 下的这种PDF文件,标题接表格的.

目前只能适用一些正常的封闭表格,如果leader还有要求适配别的表格类型(非封闭, 图片等)我再更新.同时欢迎更新适配其他表格并提交PR!

## 使用方法
参照 [main.py](main.py) 中的调用即可.

## 具体文档
模块的具体文档在模块目录中.[模块文档](./PDFExtractor/README.md)

## 其他说明
这个项目是小学期帮项目组做的，分享出来。我只是个本科生，所以如果写的差请批评指教！感激不尽！

## 更新记录
1. 2020/6/24 优化算法以解决标题被识别成表格内容、表格出现空行而引发的错误