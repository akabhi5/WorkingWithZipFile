import zipfile
''' working with zip files with zipfile module with this module we 
    can work with individual files too but we can't work with gzip file '''

with zipfile.ZipFile('files.zip', 'w', compression=zipfile.ZIP_DEFLATED) as my_zip:
    my_zip.write('abc.txt')
    my_zip.write('xyz.txt')