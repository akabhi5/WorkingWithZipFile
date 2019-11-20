import zipfile
''' working with zip files with zipfile module with this module we 
    can work with individual files too but we can't work with gzip file '''

with zipfile.ZipFile('files.zip', 'r') as my_zip:
    # print(my_zip.namelist()) prints list of files in zip file
    my_zip.extractall('files') # extracts to a folder named files
    my_zip.extract('abc.txt') # to extract select file only from a zip file
