import os
import re

def main():
    list = []
    list_formatted = []
    _text = ''
    with open('file.txt') as f:
        f_contents = f.readlines()
        for line in f_contents:
            if not line.isspace():
                list.append(line.strip())
        for line in list:
            # if str(line) in (r'transitions:', r'[-->]', r'end.'):
            if re.search(r'end.', str(line)) or re.search(r'transitions:', str(line)) or re.search(r'-->', str(line)):
                _text += str(line)
                if re.search(r'end.', str(line)):
                    list_formatted.append(_text)
            else:
                list_formatted.append(str(line))
    for line in list_formatted:
        print(line)
    print(len(list_formatted))

if __name__ == '__main__':
    main()


