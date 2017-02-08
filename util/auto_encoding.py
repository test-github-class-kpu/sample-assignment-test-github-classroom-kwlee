# coding: utf-8
import os
import sys


def main(argv):
    start_path = os.path.abspath(os.curdir)
    # decide root_path
    if len(argv) > 1:
        root_path = argv[1]
    else:
        root_path = os.path.abspath(os.pardir)
    # if something goes wrong
    try:
        os.chdir(root_path)
        recursively_add_header(root_path)
    except BaseException as e:
        os.chdir(start_path)
        raise e


def recursively_add_header(path):

    header_str = '''# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이 사용되었다는 점을 표시하는 것임
# [학번] [이름]
# 각 행의 자세한 주석을 추가하시오
'''
    print(header_str)
    for root, dirnames, filenames in os.walk(path):
        print("* root = %s" % root)
        for filename in filenames:
            full_path = os.path.join(root, filename)
            print("** full_path = %s" % full_path)


if __name__ == '__main__':
    main(sys.argv)
