A simple implementation of the Lempel-Ziv Welch compression algorithm.

###Usage:

To run, use command 

```
    python3 lzw.py <input file>
```

where 'input file' is a txt file. The program will print a report of the compression/decompression process.
It will also produce three output files 

```
    original-FILENAME-XXXXX.txt
    compressed-FILENAME-XXXXX.txt
    decompressed-FILENAME-XXXXX.txt
```
where FILENAME is the name of the input file and XXXXX is a random string of bytes. 
To clear these output files, which build up over repeated use, from the directory, run

```
    sh clean.sh
```
