#!/usr/bin/python3
""" reads stdin line by line and computes metrics """

import sys

t_size = 0
counter = 0


S_code = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}

try:

    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            i = line_list[-2]
            size = int(line_list[-1])
            if i in S_code.keys():
                S_code[i] += 1
            t_size += size
            counter += 1

            if counter == 10:
                counter = 0
                print('File size: {}'.format(t_size))
                for key, value in sorted(S_code.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(t_size))
    for key, value in sorted(S_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
        else:
            pass
