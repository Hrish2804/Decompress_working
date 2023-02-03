# create a file to decompress a compressed file?

import zipfile
with zipfile.ZipFile('imagepro.zip', 'r') as zip_ref:
    zip_ref.extractall()