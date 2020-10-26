import argparse
import os

def show_hex(bin):
    count = 0
    print("-------------hex show--------------")

    for binary in bin:
        if (count > 0) and (count % 0x10 == 0):
            print("\n", end = '')
            
        print("%02x " % binary, end = '')

        count += 1

    print("\n-------------hex show--------------")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='binary file tail to hex.',
        epilog="Example: python3 ./bintail.py -in input.bin -a [show/cut] -n 32 ")
    parser.add_argument('-i', '--input', dest='input', required=True, help='input file')
    parser.add_argument('-a', '--action', dest='action', required=True, default='slow', help='[show/cut] file')
    parser.add_argument('-n', '-num', dest='number', required=True, default=32, type=int, help='number')
    args = parser.parse_args()

    fsize = os.path.getsize(args.input)

    with open(args.input, 'rb') as inFile:
        if "show" == args.action:
            if fsize >= args.number:
                inFile.seek(-1 * args.number, 2)

            show_hex(inFile.read())
        elif "cut" == args.action:
            if fsize >= args.number:
                inFile.seek(-1 * args.number, 2)

            with open("output/output.bin", 'wb') as outFile:
                outFile.write(inFile.read())
