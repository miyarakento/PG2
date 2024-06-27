#! python3
# bulletPointAdder.py

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    linus[i] = '*' + lines[i]
text = '\n'.join(linus)

pyperclip.copy(text)
