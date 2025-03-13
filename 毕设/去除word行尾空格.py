# encoding: utf-8
'''
@author: Sawyer
@license: None
@contact: 2395967268@qq.com
@file: 去除word行尾空格.py
@time: 2025/3/11
@desc:去除pdf转word后每行尾部的空格
'''
import os
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.oxml.ns import qn
from docx.shared import Pt, Inches

import string

def is_chinese(uchar):
    if uchar.isdigit() or uchar in string.ascii_letters or uchar in string.punctuation:
        return False
    else:
        return True


def get_file_list(path):
    '''
    获取待处理文本路径列表
    :param path: 待处理文本根目录
    :return: 待处理文本路径列表
    '''
    file_lis = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.split(".")[-1] in ["doc", "docx"]:
                full_path = os.path.join(root, file)
                file_lis.append(full_path)
    return file_lis

def remove_end_space(file_list):
    # 读取原始docx的内容，并将每行尾部的空格删除，注意每行头部的空格不删除，然后保存
    for file in file_list:
        doc = Document(file)
        for para in doc.paragraphs:
            # 删除多余的run，如果当前run的text里只有空格，且上一个run的末尾和下一个run的开头是中文，则删除
            # 由于para.runs是个列表，这么删除会出现索引bug，因为删除了前面的索引后影响序列的遍历，后面的索引就变了
            # 1.将para.runs转换为list
            # 2.从后向前遍历
            num_runs = len(list(para.runs))
            for i in range(1, num_runs-1):
                if len(para.runs[i].text) == 0:
                    continue
                if para.runs[i].text.isspace():
                    if len(para.runs[i-1].text) == 0 or \
                       len(para.runs[i+1].text) == 0 or \
                       is_chinese(para.runs[i-1].text[-1]) or\
                       is_chinese(para.runs[i+1].text[0]):
                        para.runs[i].text = ""                    
                    continue
                if ' ' in para.runs[i].text: 
                    words = [_ for _ in para.runs[i].text.split(' ') if _ != '']
                    if len(words) < 1:
                        continue
                    new_text = words[0]
                    for j in range(1, len(words)):
                        add_char = '' if (is_chinese(words[j][0]) or is_chinese(words[j-1][-1])) else ' '
                        new_text += (add_char + words[j])
                    para.runs[i].text = new_text
                
        new_file = file.split(".")[0] + "_new.docx"
        doc.save(new_file)

if __name__ == '__main__':
    path = R"D:\Workspace\workspace_vscode_python\ExcelLib\数据\word"
    file_list = get_file_list(path)
    remove_end_space(file_list)




