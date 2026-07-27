from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.styles import Alignment

wb = Workbook()
ws = wb.active

a = ws.cell(1, 1)
a.value = '冰冷的希望'
# 字体样式
f = Font(name='微软雅黑', size=10, color='080808', bold=False, italic=False, strike=False, underline='single')

a.font = f

ws.row_dimensions[2].height = 30
ws.column_dimensions['B'].width = 20

# 单元格格式horizontal水平对齐 vertical上下对其 text_rotation字体旋转 wrap_text换行 shrinkToFit更改字体大小适配单元格 indent缩进
d = Alignment(horizontal='left', vertical='top', text_rotation=0, wrap_text=False, shrinkToFit=False, indent=0)
a.alignment = d

wb.save(r'C:\Users\肖阿强\Desktop\test.xlsx')
