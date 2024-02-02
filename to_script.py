import json
from pathlib import Path
import traceback

translated_folder = Path("translated")
origin_script_folder = Path("script-json")
new_script_folder = Path("translated_local")

names = {
    "美術教師": "美术教师",
    "麗華": "丽华",
    "藍": "蓝",
    "マスター": "主人",
    "紗希": "纱希",
    "美術商": "美术商",
    "フリッドマン": "弗里曼",
    "桜子": "樱子",
    "ルリヲ": "露莉莴",
    "鈴菜": "铃菜",
    "寧": "宁",
    "片貝": "片贝",
    "ノノ未": "乃乃未",
    "心鈴": "心铃",
    "揚げ物屋": "炸物店",
    "ルーアンの校長": "卢安校长",
    "霧乃": "雾乃",
    "女性教員": "女教师",
    "静流&藍": "静流&蓝",
    "看護師": "护士",
    "魚屋": "鱼店",
    "メイド": "女仆",
    "直哉&心鈴": "直哉&心铃",
    "女教師": "女教师",
    "優美": "优美",
    "トーマス": "托马斯",
    "司会者": "司会者",
    "麗华": "丽华",
    "鳥谷": "鸟谷",
    "弓張": "弓张",
    "氷川": "冰川",
    "藍＆直哉": "蓝&直哉",
    "キマイラ": "奇美拉",
    "櫻達の灰色の足跡": "樱花们的灰色足迹",
    "櫻達の色彩の足跡": "樱花们色彩的足迹",
    "櫻達の足跡": "樱花们的足迹",
    "吉沢緑寺": "吉泽绿寺",
    "吉沢": "吉泽",
    "女生徒A": "女学生A",
    "女生徒": "女学生",
    "男子生徒A": "男学生A",
    "男子生徒B": "男学生B",
    "男子生徒C": "男学生C",
    "男子生徒": "男学生",
    "女子生徒A": "女学生A",
    "女子生徒B": "女学生B",
    "女子生徒C": "女学生C",
    "女子生徒D": "女学生D",
    "女子生徒": "女学生",
    "校長": "校长",
    "若者": "年轻人",
    "若者男A": "青年A",
    "若者男B": "青年B",
    "若者男C": "青年C",
    "若者女A": "女士A",
    "若者女B": "女士B",
    "層": "层",
    "使用人": "佣人",
    "スタッフ": "工作人员",
    "救急隊員": "救护员",
    "警備員": "保安人员",
    "動画": "动画",
    "教師": "教师",
    "子供": "孩子",
    "黒服": "黑衣人",
    "黒服Ａ": "黑衣人A",
    "黒服B": "黑衣人B",
    "黒服C": "黑衣人C",
    "審査員A": "评委A",
    "審査員B": "评委B",
}

unique_names = set()

# chatgpt翻译时可能会出现繁体字，这里将繁体字转换为简体字。所以翻译后文本中的人名也需要替换。
for file in translated_folder.iterdir():
    basename = file.name
    file_path = translated_folder / file.name
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            translated_datas = json.load(f)

        origin_file_path = origin_script_folder / basename
        with open(origin_file_path, "r", encoding="utf-8") as f:
            origin_datas = json.load(f)

        # iterate over each message, raise error if length not equal
        for origin_data, translated_data in zip(
            origin_datas, translated_datas, strict=True
        ):
            assert len(translated_data) == 1
            # read translated message
            ripe = list(translated_data.values())[0]
            # fix names in message
            for original_name, new_name in names.items():
                ripe = ripe.replace(original_name, new_name)
            # remove line break and
            # replace message in origin data
            origin_data["message"] = ripe.replace("\r\n", "")

            # fix names
            if "name" in origin_data:
                # if name in names, replace it; otherwise keep it
                origin_data["name"] = names.get(
                    origin_data["name"], origin_data["name"]
                )
                unique_names.add(origin_data["name"])
            if "names" in origin_data:
                origin_data["names"] = [
                    names.get(name, name) for name in origin_data["names"]
                ]
                unique_names.update(origin_data["names"])

        # save file
        with open(new_script_folder / basename, "w", encoding="utf-8") as f:
            json.dump(origin_datas, f, ensure_ascii=False, indent=2)
        print(f"{basename} finished")
    except Exception as e:
        raise e
        # traceback.print_exc()

not_converted_names = unique_names - set(names.values())
if not_converted_names:
    print("Not converted names:", not_converted_names)
