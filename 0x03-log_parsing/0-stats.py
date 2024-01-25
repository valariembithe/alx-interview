#!/usr/bin/python3
""" Log parsing """
import sys


def print_statistics(file_size, status_codes):
    """ Prints out the file size and status codes in ascending order"""
    print('File size: {}'.format(file_size))
    for code in sorted(status_codes):
        print('{} : {}'.format(code, status_codes[code]))

def parsing_line(line, stats):
    """ reads stdin line by line and computes metrics"""
    try:
        components = line.split()
        if len(components) != 7 or components[2] != 'GET' or components[3] != '/projects/260' or components[4] != 'HTTP/1.1':
            return
        status_code = int(components[5])
        file_size = int(components[6])

        stats["total_size"] += file_size
        stats['line_count'] += 1
        stats['status_code'][status_code] = stats['status_codes'].get(status_code, 0) + 1

    except(ValueError, IndexError):
        pass

def main():
    """Main function"""
    try:
        while True:
            stats = {'total_size': 0, 'line_count': 0, 'status_codes': {}}
            for i, line in enumerate(sys.stdin, start=1):
                parsing_line(line.strip(), stats)
                    
                if i % 10 == 0:
                    print_statistics(stats['total_size'], stats['status_codes'])

    except (KeyboardInterrupt):
        pass

    print_statistics(stats['total_size'], stats['status_codes'])

if __name__ == '__main__':
    main()