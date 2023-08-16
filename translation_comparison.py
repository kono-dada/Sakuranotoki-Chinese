import os
import json

translated_folder = "translated"
untranslated_folder = "untranslated"
translated_file_list = os.listdir(translated_folder)
untranslated_file_list = os.listdir(untranslated_folder)

key_words = "贋作"
except_words = '赝作'

for i in untranslated_file_list:
    u_file_path = untranslated_folder + '\\' + i
    t_file_path = translated_folder + '\\' + i
    with open(u_file_path, 'r', encoding='utf-8') as file:
        untranslated_data = json.load(file)
    with open(t_file_path, 'r', encoding='utf-8') as file:
        translated_data = json.load(file)
    for j in range(len(untranslated_data)):
        line = list(translated_data[j].values())[0]
        if(line.find(except_words) != -1):
            continue
        line = list(untranslated_data[j].values())[0]
        if(line.find(key_words) != -1):
            print("Untranslated: " + u_file_path + ":" + str(j + 1))
            print("  " + list(untranslated_data[j].values())[0].replace('\r\n', ''))
            print("Translated: " + t_file_path + ":" + str(j + 1))
            print("  " + list(translated_data[j].values())[0].replace('\r\n', '') + '\n')