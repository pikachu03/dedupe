# Dedupe
A python script to identify duplicate files in a given directory

Please note: this library is made to be used on macos and currently only works with python 2.x.

## To Use
### Dedupe as a Library
If you would like to use dedupe as a library in your own code, copy `dedupe-v2.py` to the directory you would like to use it in and add the line `import dedupe-v2` to the beginning of your program.

#### Example
```python
# import the library
import dedupe-v2

# create a DedupeObj object. This is what you will dedupe.
myDedupeObj = dedupeObj("path/to/directory")
# call the DedupeObj dedupe method. This will dedupe the directory, 
# print the results, and place the results at path/to/directory/DUPLICATES.txt
myDedupeObj.dedupe()
```

### Dedupe From the Command Line
If you would like to use dedupe as a utility from your command line, clone or download the repository and direct your terminal to the dedupe directory. There, run `python dedupe-cli.py`. You will be prompted to enter the file path to the directory you want to dedupe. **You must enter the complete file path. Using a tilde will NOT work.** After submitting the file path, dedupe will print out it's results and provide a detailed list of the duplicates in a file that will be specified in the output.