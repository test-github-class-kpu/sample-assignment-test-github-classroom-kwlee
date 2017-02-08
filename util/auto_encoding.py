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
        root_split_path = os.path.split(root)
        # filter path
        if root_split_path[-1].startswith('ch'):
            process_path(root, filenames, header_str)


def process_path(root, filenames, header_str):
    print("* root = %s" % root)
    for filename in filenames:
        b_rewrite = False
        full_path = os.path.join(root, filename)
        with open(full_path, 'r') as f_in:
            txt_lines = f_in.readlines()
            f_in.close()

        original_length = len(txt_lines)

        # if the first line includes coding, remove it
        if is_line_encoding(txt_lines[0]):
            txt_lines.pop(0)
            b_rewrite = True

        if b_rewrite:
            print("** full_path = %s : %d -> %d" % (full_path, original_length, len(txt_lines)))
            write_lines(full_path, txt_lines)


def write_lines(full_path_string, lines):
    with open(full_path_string, 'wt') as f_out:
        f_out.writelines(lines)
        f_out.close()


def is_line_encoding(line):
    b_first_line_comment = line.startswith('#')
    b_first_line_has_coding = 'coding' in line
    return b_first_line_comment and b_first_line_has_coding


if __name__ == '__main__':
    main(sys.argv)
