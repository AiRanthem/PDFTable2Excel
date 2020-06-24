"""
所有参数化内容在这里进行修改。
"""

# 标题在PDF文件中最多有几行
TITLE_MAX_LINES = 3

# 认定是标题一部分的触发字, 该行文字是标题一部分的必要条件
TITLE_TRIGGER_WORDS = ['重点', '公示', '清单']

# 标题必定包含的关键词, 该标题确实是标题的充分条件
TITLE_KEY_WORD = '公示'

# 表格字段关键字, 如果一列的表头含有这个关键字则认为他属于这个字段
FIELD_KEY_WORDS = {
    "order": "序号",
    "id": "编号",
    "name": "名称",
    "institution": "单位",
    "principal": "负责人",
    "founds": "经费",
    "period": "实施周期"
}

# Excel的表头
WORKBOOK_HEAD = ["表格标题", "序号", "项目编号", "项目名称", "项目牵头单位", "项目负责人", "中央财政经费(万元)", "项目实施周期(年)", "所属专项"]

# Excel表格对应的数据结构字段,请对照上面写
WORKBOOK_FIELD = ['title', 'order', 'id', 'name','institution', 'principal', 'founds', 'period', 'project']
