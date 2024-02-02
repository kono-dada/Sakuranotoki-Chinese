import json
import os

folder = 'translated'
origin_script_folder = 'script-json'
new_script_folder = 'translated_local'

# list all the files in the folder
files = os.listdir(folder)

names = {
    '美術教師': '美术教师', 
    '麗華': '丽华', 
    '藍': '蓝',
    'マスター': '主人', 
    '紗希': '纱希',
    '美術商': '美术商',
    'フリッドマン': '弗里曼',
    '桜子': '樱子',
    'ルリヲ': '露莉莴',
    '鈴菜': '铃菜',
    '寧': '宁',
    '片貝': '片贝',
    'ノノ未': '乃乃未',
    '心鈴': '心铃',
    '揚げ物屋': '炸物店',
    'ルーアンの校長': '卢安校长', 
    '霧乃': '雾乃',
    '女性教員': '女教师',
    '静流&藍': '静流&蓝',
    '看護師': '护士',
    '魚屋': '鱼店',
    'メイド': '女仆',
    '直哉&心鈴': '直哉&心铃',
    '女教師': '女教师',
    '優美': '优美',
    'トーマス': '托马斯',
    '司会者': '司会者',
    '麗华': '丽华',
    '鳥谷': '鸟谷',
    '弓張': '弓张',
    '氷川': '冰川',
    'キマイラ': '奇美拉',
    '櫻達の灰色の足跡': '樱花们的灰色足迹',
    '櫻達の色彩の足跡': '樱花们色彩的足迹',
    '櫻達の足跡': '樱花们的足迹',
    '吉沢緑寺': '吉泽绿寺',
    '吉沢': '吉泽',
    '女生徒A': '女学生A',
    '女生徒': '女学生',
    '男子生徒A': '男学生A',
    '男子生徒B': '男学生B',
    '男子生徒C': '男学生C',
    '男子生徒': '男学生',
    '女子生徒A': '女学生A',
    '女子生徒B': '女学生B',
    '女子生徒C': '女学生C',
    '女子生徒': '女学生',
    '校長': '校长',
    '若者': '年轻人',
    '若者男A': '青年A',
    '若者男B': '青年B',
    '若者女A': '女士A',
    '若者女B': '女士B',
    '層': '层',
    '使用人': '佣人',
    'スタッフ': '工作人员',
    '救急隊員': '救护员',
}

# chatgpt翻译时可能会出现繁体字，这里将繁体字转换为简体字。所以翻译后文本中的人名也需要替换。
for file in files:
    file_path = folder + '\\' + file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        origin_file_path = origin_script_folder + '\\' + file
        with open(origin_file_path, 'r', encoding='utf-8') as f:
            origin_data = json.load(f)

        for i in range(len(data)):
            ripe = list(data[i].values())[0]
            for original_name, new_name in names.items():
                ripe = ripe.replace(original_name, new_name)
            origin_data[i]['message'] = ripe.replace('\r\n', '')
            if 'name' in origin_data[i].keys():
                if origin_data[i]['name'] in names.keys():
                    origin_data[i]['name'] = names[origin_data[i]['name']]
            if 'names' in origin_data[i].keys():
                for j, name in enumerate(origin_data[i]['names']):
                    if name in names.keys():
                        origin_data[i]['names'][j] = names[name]

        with open(new_script_folder + '\\' + file, 'w', encoding='utf-8') as f:
            content = json.dumps(origin_data, ensure_ascii=False, indent=2)
            f.write(content)
        print(f'{file} finished')
    except:
        pass
