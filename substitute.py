import json
import os


translated_dir = 'translated'
keywords = '路里汝'
substitution = '露莉莴'

for file in os.listdir(translated_dir):
    with open(os.path.join(translated_dir, file), 'r', encoding='utf8') as f:
        translated_text = json.load(f)
    for i, sentence in enumerate(translated_text):
        key = list(sentence.keys())[0]
        if keywords in sentence[key]:
            sentence[key] = sentence[key].replace(keywords, substitution)
            print(file)
            print(f'{i}: ' + sentence[key])
            print()
    with open(os.path.join(translated_dir, file), 'w', encoding='utf8') as f:
        s = json.dumps(translated_text, ensure_ascii=False, indent=0)
        s = s.replace('\n}', '}')
        s = s.replace('\n]', ']')
        s = s.replace('{\n', '{')
        s = s.replace('[\n', '[')
        f.write(s)

