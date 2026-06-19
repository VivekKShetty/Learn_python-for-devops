import re

text = "The quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Pattern found:", match.group())
else:
    print("pattern not found")

search = re.search(pattern, text)
if search:
     print("Pattern found:", search.group())
else:
    print("pattern not found")