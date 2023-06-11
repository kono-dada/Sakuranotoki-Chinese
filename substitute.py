import json
import os


translated_dir = 'translated'
keywords = '宫崎酥酥'  # 宫崎みすゞ 宫崎美鈴 宫崎美铃 宫崎未寄 宫崎美鶴 宫崎美鎏 宫崎美穗 宫崎美津
                        # 宫崎美珠 宫崎实苏 宫崎实铃 宫崎蜜柚 宫崎实齿 宫崎水静 宫崎未鈴 宫崎美洲雀
                        # 宫崎美酴 宫崎美洲 宫崎未译 宫崎莫忆 宫崎樱子 宮崎美寿寿 宫崎三津子 宮崎みすゞ
                        # 宮崎实久 宮崎美寿 宫崎酥酥
substitution = '宫崎心铃'

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

