import urllib.request, urllib.error
from bs4 import BeautifulSoup


def parse(filename, url):
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.title
    title = title_tag.string

    with open(filename, mode='w') as f:
        f.writelines(title + '\n')
        texts = soup.select('p')
        for test in texts:
            if(test.string != None):
                f.writelines(test.string + '\n')



#　日経のトップページをパースする
url = "http://www.nikkei.com/"

html = urllib.request.urlopen(url)

soup = BeautifulSoup(html, "html.parser")

#パースした結果からタイトルを取得する。
title_tag = soup.title
#タグなしの文字列を取得数
title = title_tag.string
#タグごと表示する。
print(title_tag)

#タイトルを表示する
print(title)

path = 'data/'

#画面内のリンクを全て取得する。
for link in soup.find_all('a'):
    address = link.get('href');
    if (address.find('http') == -1 and address[0:10].find('article') > 0):#内部リンクだけを取得する。
        #文字列から記事の一意を示す固定長だけを抽出する。
        filename = address[9:28]
        #print(url + address)
        parse(path + filename + '.txt',url + address )
