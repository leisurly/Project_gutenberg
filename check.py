import re

def check_chinese_book(text):
    #只保留中文書名
    return ''.join(re.findall(r'[\u4e00-\u9fff]', text))

def extract_chinese_sentences(text):
    return ''.join(re.findall(r'[\u4e00-\u9fff，。！？「」『』、；：（）—《》]', text))
def split_by_length(text, length):
    return [text[i:i+length] for i in range(0, len(text), length)]





