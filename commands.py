## Commands

# TODO:



import os
import sys
from PIL import Image
import strings

def conv2jpg(file_path):
    if file_path == "-h" :
        print("Использование: convert2jpg <имя_до_файла>")

    if os.path.exists(file_path):
        im = Image.open(file_path)
        target_name = file_path + ".jpg"
        rgb_im = im.convert('RGB')
        rgb_im.save(target_name)
        print(strings.conv2jpg_succ_save + target_name)
    else:
        print(file_path + strings.file_not_found)

    return 0

def habr_feed():
    pass

def main(arg_list):
    if len(arg_list) > 1:
        if arg_list[1] == "conv2jpg":
            conv2jpg(arg_list[2])
        elif arg_list[1] == "habr_feed":
            habr_feed()


    return 0

if __name__ == "__main__":
    main(sys.argv)