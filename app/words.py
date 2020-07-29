from stop_words import get_stop_words
from stop_words import safe_get_stop_words
import re

stop_words = get_stop_words('fr')
my_words = safe_get_stop_words('unsupported language')

for w in stop_words:
    my_words.append(w)

my_stop_words = ["hello", "salut"]

for w in my_stop_words:
    my_words.append(w)

test_str = input("tape un phrase?" "\n")
# regex = r"( |,)"
# subst = "\n"
# result = re.sub(regex, subst, test_str, 0, re.MULTILINE)
# if result:
#     print(result)
word = test_str.split(" ")

for w in word:
	if w not in my_words:
		print(w)
