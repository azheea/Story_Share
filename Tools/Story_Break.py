import spacy
import os
def Story_Break():
    # 加载中文模型
    nlp = spacy.load("zh_core_web_sm")
    # 读取故事文件
    with open(os.getcwd()+ "\story.txt", 'r', encoding='utf-8') as file:
        text = file.read()
    # 对文本进行分句
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    # 按逗号分隔句子为段落，并将完整的句子以逗号为分隔符换行
    paragraphs = []
    current_paragraph = ""
    for sentence in sentences:
        if "，" in sentence:
            current_paragraph += sentence.replace("，", "，\n")
            paragraphs.append(current_paragraph)
            current_paragraph = ""
        else:
            current_paragraph += sentence
    # 将拆解后的段落写入输出文件
    with open(os.getcwd()+"\log\output.txt", 'w', encoding='utf-8') as file:
        for paragraph in paragraphs:
            file.write(paragraph + '\n')