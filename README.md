# emoji-table

IMEを有効化した状態でスムーズに絵文字を打つためのローマ字テーブル

## 使い方

0. Google日本語入力をインストール
1. Google日本語入力で使用しているローマ字テーブルをエクスポート
2. romantableを生成
3. 1のファイルに結合してインポート

## romantableの生成

```console
python3 generator.py --help         
usage: generator.py [-h] [-t {0,1,2,3,4,5}]

Generate romantable

optional arguments:
  -h, --help            show this help message and exit
  -t {0,1,2,3,4,5}, --tone {0,1,2,3,4,5}
                        skin tone
```

## skin toneの設定

emojiに複数のskin toneが用意されている場合、上書きできます

`:ok_hand:`
| 0 | light=1 | medium-light=2 | medium=3 | medium-dark=4 | dark=5 |
| --- | --- | --- | --- | --- | --- |
| 👌 | 👌🏻 | 👌🏼 | 👌🏽 | 👌🏾 | 👌🏿 |
