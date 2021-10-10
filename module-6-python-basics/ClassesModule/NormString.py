# declare and set functions to normalize_string

def isspace(iter_text: iter) -> iter:
    #'' 'print spaces up to the first significant character and the character itself in uppercase' ''
    for s in iter_text:
        if s.isspace():
            yield s  # non-displayable characters (spaces)
        else:
            yield s.upper()  # to uppercase
            break  # to the first significant character

def upper_text(text: str) -> iter:
    iter_text = iter(text)
    yield from isspace(iter_text)  # first significant character of text to uppercase
    for s in iter_text:
        yield s.lower()
        if s == '.':  # significant character after '.' to uppercase
            yield from isspace(iter_text)


def normalize_string(string):
    return ''.join(upper_text(string))