# README

## 说明

主要用于分析二进制文档，文档很大，经常只是查看文件末尾的签名内容，需要查看HEX内容

## 使用

`python3 bintail.py --help`

```
usage: bintail.py [-h] -i INPUT -a ACTION -n NUMBER

binary file tail to hex.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        input file
  -a ACTION, --action ACTION
                        [show/cut] file
  -n NUMBER, -num NUMBER
                        number

Example: python3 ./bintail.py -in input.bin -a [show/cut] -n 32
```