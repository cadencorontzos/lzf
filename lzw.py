
# +++++++++ LZW Compression +++++++++
# Implementation by Caden Corontzos, Oct. 2021
# See Lisence for terms of use

import sys
import time
import random
import os
import math

"""
    COMPRESS AND DECOMPRESS: both funtions take the name of the file they are meant to operate on, and the name of the file they are meant to write to.
    The initial dictionary should vary by type of data. Generally, it should have at least the base characters of the file type.
"""

def compress(filename, newFileName):
    codebook    = {chr(i).encode():i for i in range(256)}
    file        = open(filename, 'rb')
    newFile     = open(newFileName, 'wb')
    codeword    = 256
    
    nextChar = file.read(1)
    currentBlock = ''.encode()
    while nextChar:  
        if (currentBlock+nextChar) in codebook:
            currentBlock+=nextChar
        else:
            possibleCodeLength = math.ceil(math.log(codeword,2)/8)
            newFile.write(codebook[currentBlock].to_bytes(possibleCodeLength, 'big'))
            newFile.write(nextChar)
            codebook[currentBlock+nextChar] = codeword
            codeword+=1
            currentBlock = ''.encode()
        nextChar = file.read(1)
    if currentBlock != '':
        newFile.write(codebook[currentBlock].to_bytes(possibleCodeLength, 'big'))
    file.close()
    newFile.close()

def decompress(compressedFileName, newFileName):
    codebook    = {i:chr(i).encode() for i in range(256)}
    file        = open(compressedFileName, 'rb')
    newFile     = open(newFileName, 'w')
    codeword    = 256
    
    nextChar = file.read(1)
    currentBlock = ''.encode()
    while nextChar:  
        possibleCodeLength = math.ceil(math.log(codeword,2)/8)
        if len(currentBlock) < possibleCodeLength:
            currentBlock+=nextChar
        else:

            index = int.from_bytes(currentBlock,'big')
            theByte = codebook[index]
            theAdditionalByte = nextChar.decode()
            newFile.write(theByte.decode())
            newFile.write(theAdditionalByte)
            codebook[codeword] = theByte+nextChar
            codeword+=1
            currentBlock = ''.encode()
        nextChar = file.read(1)
    if currentBlock:
            index = int.from_bytes(currentBlock,'big')
            theByte = codebook[index]
            newFile.write(theByte.decode())

    file.close()
    newFile.close()

"""
    HELPER METHODS: These methods make for a clean report generation

"""

def printHeader(what):
    print('------------------------------------------------------------------------------')
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
    rate = compressed/original
    print('The compression rate was ' + str(rate) + '.')

def makeFilename(which, filename):
    return which +'-'+filename+'-'+str(randSuffix) + '.txt'

def assertCorrectness(originalFile, decompressedFile):
    oFileData = open(originalFile)
    oFile = oFileData.read()
    dFileData = open(decompressedFile)
    dFile = dFileData.read()
    if oFile==dFile:
        print('The originial file and the decompressed file are the same.')
    else:
        print('Decomp error: The originial file and the decompressed file are not the same.')
    
def printFooter(names):
    print('------------------------------------------------------------------------------')
    print('To see the three versions of the file, see ', end = '')
    print(*names, sep=', ', end='.\n')


"""
    REPORT GENERATION: On command line call, the name of the file is taken in. The file is compressed, then decompressed. The logistics of this process 
    are printed to the console, the compressed and decompressed files are output into the directory, and the correctness of the algorithm is checked.

"""

if __name__ == "__main__":
    randSuffix = random.randint(10000,20000)
    names = []
    filename = sys.argv[-1]

    printHeader(filename)


    #original
    printHeader('original')
    fileData = open(filename)
    original = reportSize(filename, 'original')
    originalFileName = makeFilename('original', filename)
    names.append(filename)

    #compression
    printHeader('compression')
    compressedFileName = makeFilename('compressed', filename)
    names.append(compressedFileName) 
    start = time.time()
    compress(filename, compressedFileName)
    end = time.time()
    reportTime(start, end, 'compression')
    reportSize(compressedFileName, 'compressed')
    reportCompressionRate(filename, compressedFileName)

    #decompression
    printHeader('decompression')
    decompressedFileName = makeFilename('decompressed', filename)
    start = time.time()
    decompress(compressedFileName, decompressedFileName)
    end = time.time()
    names.append(decompressedFileName)
    reportTime(start, end, 'decompresssion')
    reportSize(decompressedFileName, 'decompressed')
    assertCorrectness(filename,decompressedFileName)

    printFooter(names)