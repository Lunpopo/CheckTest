# encoding: utf8
#!/usr/bin/env python
# @author Lunpopo
import os
import sys
import subprocess
from argparse import ArgumentParser
from termcolor import colored
import re


check_point_key = [
    'test',
    'test code',
    'test end',
    'test point',
    'this is test code',
    'test block'
]


def banner():
    banner = """
     #####                              #######                     
    #     # #    # ######  ####  #    #    #    ######  ####  ##### 
    #       #    # #      #    # #   #     #    #      #        #   
    #       ###### #####  #      ####      #    #####   ####    #   
    #       #    # #      #      #  #      #    #           #   #   
    #     # #    # #      #    # #   #     #    #      #    #   #   
     #####  #    # ######  ####  #    #    #    ######  ####    #   
    """
    print colored(banner, 'white')


def get_all_files(dir):
    file_path_list = []
    list = os.listdir(dir)
    for i in range(0, len(list)):
        path = os.path.join(dir, list[i])
        if os.path.isdir(path):
            file_path_list.extend(get_all_files(path))
        if os.path.isfile(path):
            file_path_list.append(path)
    return file_path_list


def main():
    """
    main function
    :return None
    """
    parser = ArgumentParser()

    # get directory module
    get_directory = parser.add_argument_group('get directory module', "get directory")
    get_directory.add_argument('-d', '--directory', nargs='+', dest='directory', metavar='PATH', help='input directory path you want to check')

    # extend options module
    extend_options = parser.add_argument_group('extend module', 'extend command options')
    extend_options.add_argument('-e', '--file-extend', dest='file_extend', metavar='REGULAR', help='input file extend you wanna check and this option support regular expression, for example -> "*.py" or "*.html"')
    extend_options.add_argument('-c', '--check-point', dest='check_point', metavar='CHECK-STRING', help='input the key check point you want to find out and this option support regular expression, for example -> "test|test code|test end"')

    # filter module 
    filter_options = parser.add_argument_group('filter module', 'filter command output module')
    filter_options.add_argument('-f', '--filter', dest='filter', metavar='REGULAR-STRING', help='filter you do not want to see and this option support regular expression, for example -> "test case | test code"')

    opts = parser.parse_args()

    banner()
    if not sys.argv[1:]:
        parser.print_help()
    else:
        try:
            if opts.directory:
                for check_path in opts.directory:
                    #fuck = get_all_files(check_path)
                    #for i in fuck:
                    #    print i
                    file_extend = opts.file_extend
                    check_point = opts.check_point
                    if not file_extend:
                        file_extend = '*.*'
                    if not check_point:
                        check_point = "|".join(check_point_key)

                    # 如果有 --filter option, 就追加命令
                    if not opts.filter:
                        examine_command = 'find {} -name "{}" | xargs grep -niE --color "{}" 2>/dev/null'.format(check_path, file_extend, check_point)

                        # return code value just 0 and 256
                        return_code = os.system(examine_command)
                        if return_code == 0:
                            pass
                        elif return_code == 256:
                            print colored('Do not match any code you input! Trying to use -e option or do not use *.* expression', 'red')

                    else:
                        # 这是有 --filter option 过滤的情况
                        examine_command = 'find {} -name "{}" | xargs grep -niE "{}" 2>/dev/null | grep -ivE "{}"'.format(check_path, file_extend, check_point, opts.filter)

                        p = subprocess.Popen(examine_command, stdout=subprocess.PIPE, shell=True)
                        (stdout, stderr) = p.communicate()
                        returncode = p.returncode

                        check_point_case = check_point.split('|')
                        for _ in check_point_case:
                            stdout = re.sub(re.compile(_, re.I), colored(_, 'cyan'), stdout)
                        print stdout

            # 逻辑判断，如果只有 -filter option 而没有 -d option, 就抛出错误
            if opts.filter and not opts.directory:
                print colored('please use -d option first before hit -f option', 'red')
                sys.exit(1)
        except Exception as e:
            print e
            

if __name__ == '__main__':
    main()
