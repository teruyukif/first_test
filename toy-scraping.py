import urllib.request, urllib.error
from bs4 import BeautifulSoup

#　日経のトップページをパースする
url = "http://www.nikkei.com/"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

#パースした結果からタイトルを取得する。
title_tag = soup.title
#タグなしの文字列を取得数
title = title_tag.string
#タグごと表示する。
#print(title_tag)

#タイトルを表示する
#print(title)

#画面内のリンクをしゅべて取得する。
#for link in soup.find_all('a'):
#    print(link.get('href'))

# 画面内の文章を全て取得する
print(soup.get_text())
