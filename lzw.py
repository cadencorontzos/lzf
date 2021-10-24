
# +++++++++ LZW Compression ++++++++++++
# Implementation by Caden Corontzos, Oct. 2021
# See Lisence for terms of use

import sys
import time
import random

def compress(text):
    return('test')

def decompress(text):
    return('test')

def printSample(text, which):
    print('_____________________________________________')
    print('Here is a sample of the ' + which + ' file.')
    print(text[1000:1500])
    print('_____________________________________________')

def reportSize(text, which):
    size = len(text.encode('utf-8'))
    print('The size of the ' + which + ' file is '+ str(size) + ' bytes.')
    return size

def reportTime(start, end, what):
    totalTime = end - start
    print('The time of ' + what + ' was ' + str(totalTime) + ' seconds.')

def reportCompressionRate(original, compressed):
    rate = original/compressed
    print('The compression rate was ' + str(rate) + '.')

def generateOutputFile(which, filename):
    f= open( which +'-'+filename+'-'+str(randSuffix) + '.txt', 'w')
    f.write(file)
    f.close()

# generates a report of the compression/decompression process of a given file
if __name__ == "__main__":
    randSuffix = random.randint(10000,20000)

    #original
    filename = sys.argv[-1]
    fileData = open(filename)
    file = fileData.read()
    original = reportSize(file, 'original')
    printSample(file,'original')
    generateOutputFile('original',filename)

    #compression
    start = time.time()
    compressedFile = compress(file)
    generateOutputFile('compressed', filename)
    end = time.time()
    reportTime(start, end, 'compression')
    compressed = reportSize(compressedFile, 'compressed')
    reportCompressionRate(original, compressed)
    printSample(compressedFile, 'compressed')


    #decompression
    start = time.time()
    decompressedFile = decompress(compressedFile)
    generateOutputFile('decompressed', filename)
    end = time.time()
    reportTime(start, end, 'decompresssion')
    printSample(decompressedFile, 'decompressed')
