import json

with open("output.txt", "r", encoding="utf-8") as input_file:
    data = input_file.read()


data_json = json.loads(data)

sentences = data_json["Result"]["Sentences"]
extracted_text = [sentence["Text"] for sentence in sentences]

# 将提取的文本内容写入新文件
with open("extracted_text.txt", "w", encoding="utf-8") as output_file:
    for text in extracted_text:
        output_file.write(text + "\n")
