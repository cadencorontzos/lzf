
# LZW Compression
# Implementation by Caden Corontzos, Oct. 2021
# See Lisence for terms of use

import sys

def compress(text):
    return('test')

def decompress(text):
    return('test')

def printSample(text, which):
    print('_____________________________________________')
    print('Here is a sample of the ' + which + ' file.')
    print(text[1000:1500])
    print('_____________________________________________')

if __name__ == "__main__":
    #
    filename = sys.argv[-1]
    fileData = open(filename)
    file = fileData.read()
    printSample(file,'original')
    compressedFile = compress(file)
    printSample(compressedFile, 'compressed')
    decompressedFile = decompress(compressedFile)
    printSample(decompressedFile, 'decompressed')
