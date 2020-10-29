#!/usr/bin/env python3

import argparse
import os

def show_hex(bin):
    count = 0

    print("----------------------hex show-----------------------")

    # colum index
    for index in range(0, 0x10):
        if (index % 0x10 == 0):
            print(" r\\c", end = '')
        print(" %02x" % index, end = '')
    print("\n", end = '')

    for binary in bin:
        # row line
        if (count > 0) and (count % 0x10 == 0):
            print("\n", end = '')

        # row index
        if (count % 0x10 == 0):
            print("%04x" % count, end = '')
            
        # data
        print(" %02x" % binary, end = '')

        count += 1
    print("\n", end = '')

    print("----------------------hex show-----------------------")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='binary file tail to hex.',
        epilog="Example: python3 ./bintail.py -in input.bin -a [tail/head/sign/content] -n 32 ")
    parser.add_argument('-i', '--input', dest='input', required=True, help='input file')
    parser.add_argument('-a', '--action', dest='action', required=False, default='show', help='[tail(hex tail)/head(hex head)/sign(sign bin)/content(content bin)] of file')
    parser.add_argument('-n', '-num', dest='number', required=False, default=32, type=int, help='number')
    parser.add_argument('-o', '-output', dest='output', required=False, default='output.bin', type=str, help='output file')
    args = parser.parse_args()

    fsize = os.path.getsize(args.input)

    with open(args.input, 'rb') as inFile:
        if "tail" == args.action:
            if fsize >= args.number:
                inFile.seek(-1 * args.number, 2)

            show_hex(inFile.read())
        elif "head" == args.action:
            if fsize < args.number:
                args.number = fsize

            show_hex(inFile.read(args.number))
        elif "sign" == args.action:
            if fsize >= args.number:
                inFile.seek(-1 * args.number, 2)

            with open(args.output, 'wb+') as outFile:
                outFile.write(inFile.read())
        elif "content" == args.action:
            readSize = 0

            if fsize > args.number:
                readSize = fsize - args.number
                with open(args.output, 'wb+') as outFile:
                    outFile.write(inFile.read(readSize))
            else:
                print("file length short")
