#! python3
# mclip.py
TEXT = {'agree':'そうですね。私も賛同します。それが良いと思います。',
        'busy': 'すみませんが、今週後半か来週にしていただけませんか',
        'upsell': 'これを毎月の寄付にすることを検討していただけませんか？' }
import sys
import pyperclip
if len(sys.agrv) < 2:
    print('使い方: python mclip.py [キーフレーズ名]')
    print('キーフレーズに対応するテキストをクリップボード日コピーしました')
    sys.exit()

 keyphrase = sys.agrv[1]   
    　　 　　　　 
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print(keyphrase + 'のテキストをクリップボードにコピーしました')
else:
    print(keyphrase + 'に対応するテキストはありません ')　
