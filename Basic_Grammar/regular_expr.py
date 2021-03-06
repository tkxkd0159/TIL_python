import re

def func_annotation(*args: "unlimit arguments", num: int = 3, **kwargs: "unlimit keyword-values") -> None:
    """
    Test function annotation

    Returns:
        None
    """
    keys, values = [], []
    for key, value in kwargs.items():
        keys.append(key)
        values.append(value)

    print(args, num)
    print("key : ", keys, "value : ", values)
    return None

DATA = """
moon 800905-1049118
kim 700905-1059119
"""

PAT = re.compile(r"([a-zA-Z]+)\s+([0-9]+)[-](\d+)")
# MATCHES_ALL = PAT.match("moon 800905-1049118")
# MATCHES_ALL = PAT.search(DATA)
# MATCHES_ALL = PAT.findall(DATA)
MATCHES_ALL = PAT.finditer(DATA)

if MATCHES_ALL:
    for iter_ in MATCHES_ALL:
        print('Match found: ', iter_.group())
else:
    print('No match')

print(PAT.sub(r"\g<1> ******-\g<3>", DATA))


TRASH = 2
AREPL_FILTER = ['trash']
#$end

print("test end")
print("test end2")

print("")
print("Function annotation")
func_annotation(1, 2, 3, num=100, A='Geeks', B='Nerds')
print(func_annotation.__annotations__)
