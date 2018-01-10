import re

"""============================================================================
    Clean Text from weird symbols
============================================================================"""
# Tokenisation without ponctuation
def clean_symbols(text):
    art = text.replace('?', '.')
    art = art.replace('!', '.')
    art = art.replace('…', '.')
    art = re.sub(r'[A-Za-z]’', ' ', art)
    art = re.sub(r'[A-Za-z]\'', ' ', art)
    art = re.sub(r'[^\w\s\._]', '', art, re.UNICODE)
    return art