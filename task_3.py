import os


def join_files(folder_name):
    files_list = os.listdir(folder_name)
    files_dict = {}
    for file in files_list:
        doc = open(folder_name + "\\" + file, encoding='utf-8')
        files_dict[len(doc.readlines())] = file
        doc.close()
    keys_list = list(files_dict.keys())
    keys_list.sort()
    for key in keys_list:
        result = open('result.txt', 'at', encoding='utf-8')
        doc = open(folder_name + "\\" + files_dict[key], encoding='utf-8')
        result.write(f'{files_dict[key]}\n')
        result.write(f'{key}\n')
        counter = 0
        while counter <= key:
            line = str(doc.readline())
            result.write(line)
            counter += 1
        result.close()
        doc.close()
    return


join_files(r"C:\Users\marin\Desktop\HomeWorks\18.06.21\sorted_task3")
