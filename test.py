import unicodedata

def normalize_filename(filename):
    return unicodedata.normalize('NFKD', filename).encode('utf-8', 'ignore').decode('utf-8')

name = '2018_FA_Ave Rapiña_Subida (1).JPG'

print(normalize_filename(name))

