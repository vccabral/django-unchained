import re

def slugify(str_base):
    str_base = str(str_base).lower()
    return re.sub(r'\W+','-',str_base)