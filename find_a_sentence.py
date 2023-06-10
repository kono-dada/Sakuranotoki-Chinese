import json
import os


translated_dir = 'translated'
keywords = '宫崎'
nkeywords = []

for file in os.listdir(translated_dir):
    with open(os.path.join(translated_dir, file), 'r', encoding='utf8') as f:
        translated_text = json.load(f)
    for i, sentence in enumerate(translated_text):
        if keywords in list(sentence.values())[0]:
            # print(file)
            print(f'{i}: ' + list(sentence.values())[0])
            # print()