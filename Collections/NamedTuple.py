import collections

import collections
import os
def main():
    file_info = collections.namedtuple('FileInfo', 'filename size date')
    root_dir = r'c:\testing'
    for _, _, file_list in os.walk(root_dir):
        for fname in file_list:
            files = [file_info(fname,
                               os.path.getsize(root_dir+"\\"+fname),
                               os.path.getctime(root_dir+"\\"+fname))
                     for fname in file_list]
    print(files[-1].filename, files[-1].size)

if __name__ == '__main__':
    main()