
# +++++++++ LZW Compression ++++++++++++
# Implementation by Caden Corontzos, Oct. 2021
# See Lisence for terms of use

import sys
import time
import random
import os

def compress(filename, newfilename):
    codebook = {}
    file = open(filename, 'r')
    newFile = open(newfilename, 'w')
    codeword = 0
    nextChar = file.read(1)
    currentBlock = ''
    #does this run too many times?
    while nextChar:
        currentBlock = str(currentBlock) + nextChar
        if codebook.get(currentBlock):
            currentBlock = codebook.get(currentBlock)
        else:
            codebook[currentBlock] = codeword
            codeword+=1
            newFile.write(currentBlock)
            currentBlock = ''
        nextChar = file.read(1)
    file.close()
    newFile.close()

def decompress(filename, newFileName):
    return('test')

def printHeader(what):
    print('---------------------------------------')
    print(what.upper()+':')

def reportSize(filename, which):
    size = os.path.getsize(filename)
    print('The size of the ' + which + ' file is '+ str(size) + ' bytes.')
    return size

def reportTime(start, end, what):
    totalTime = end - start
    print('The time of ' + what + ' was ' + str(totalTime) + ' seconds.')

def reportCompressionRate(originalFileName, compressedFileName):
    original = os.path.getsize(originalFileName)
    compressed = os.path.getsize(compressedFileName)
    rate = original/compressed
    print('The compression rate was ' + str(rate) + '.')

def makeFilename(which, filename):
    return which +'-'+filename+'-'+str(randSuffix) + '.txt'

def printFooter(names):
    print('---------------------------------------')
    print('To see the three versions of the file, see ', end = '')
    print(*names, sep=', ', end='.\n')

# generates a report of the compression/decompression process of a given file
if __name__ == "__main__":
    randSuffix = random.randint(10000,20000)
    names = []

    #original
    printHeader('original')
    filename = sys.argv[-1]
    fileData = open(filename)
    file = fileData.read()
    original = reportSize(filename, 'original')
    originalFileName = makeFilename('original', filename)
    f= open(originalFileName, 'w')
    f.write(file)
    f.close()
    names.append(originalFileName)

    #compression
    printHeader('compression')
    compressedFileName = makeFilename('compressed', filename)
    names.append(compressedFileName) 
    start = time.time()
    compressedFile = compress(filename, compressedFileName)
    end = time.time()
    reportTime(start, end, 'compression')
    reportSize(compressedFileName, 'compressed')
    reportCompressionRate(filename, compressedFileName)

    #decompression
    printHeader('decompression')
    decompressedFileName = makeFilename('decompressed', filename)
    start = time.time()
    decompressedFile = decompress(compressedFileName, decompressedFileName)
    end = time.time()
    names.append(decompressedFileName)
    reportTime(start, end, 'decompresssion')
    # reportSize(decompressedFileName, 'decompressed')

    printFooter(names)