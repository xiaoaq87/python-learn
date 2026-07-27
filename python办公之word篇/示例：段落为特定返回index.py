from docx import Document

def get_paragraph_index(doc, target_text):
    for index, paragraph in enumerate(doc.paragraphs):
        if paragraph.text.strip() == target_text.strip():
            return index
    return None  # 未找到时返回None

# 示例用法
doc = Document(r'C:\Users\肖阿强\Desktop\练习.docx')
target_text = "这是目标段落"
index = get_paragraph_index(doc, target_text)
if index is not None:
    print(f"段落内容为'{target_text}'的索引是：{index}")
else:
    print("未找到匹配段落")