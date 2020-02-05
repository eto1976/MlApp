import os
import sys
import time
import urllib.request
import ssl
context = ssl.create_default_context()

import bs4

# ダウンロードパス
dwFilePath = '"C:/Project/MlApp/data/dw/"'

class WebCrawlerLogic:
    # パラメータ定義前提
    # self = url
    def crawring(self, extensions):
        """
            Content:
                クローリング
            Param:
                self(url):        クローリングするURL
                extensions:    取得するリソースの拡張子(list)
        """
        # 指定したURLのHTMLを取得
        html = WebCrawlerLogic.get_html_string(self)
        if len(html) < 1:
            return "HTMLが取得できませんでした、URLを確認してください。"

        # リソース取得
        msg = WebCrawlerLogic.get_resource(html, extensions)
        return msg

    @staticmethod
    def get_resource(html, extensions):
        """
            Content:
                リソース取得
            Param
                html:        HTML
                extensions    拡張子のリスト
        """

        msg = ""
        resource_list = []

        # HTMLをsoupで取得後にaタグでループして、aタグ内のhrefを取得。リンク先画像の取得
        # オリジナルソースのタグ(tag)は"a"で要素(element)は"href"
        soup = bs4.BeautifulSoup(html)
        for tag in soup.find_all("img"):
            element = tag.get("src")
            try:
                # 取得するHTML要素に対してファイル名(path)と拡張子(ext)に分割
                (path, ext) = os.path.splitext(element)
                if ext in extensions:
                    resource_list.append(element)
            except Exception as e:
                print(e)
                pass

        resource_list = sorted(set(resource_list), key=resource_list.index)
        if len(resource_list) > 0:

            for resource in resource_list:
                try:
                    print("ダウンロード実施 ---> [%s]" % os.path.basename(resource))
                    msg = msg +"ダウンロード実施 ---> [%s]" % os.path.basename(resource) + "\n"
                    request = urllib.request.urlopen(resource,context=context)
                    f = open(dwFilePath + os.path.basename(resource), "wb")
                    f.write(request.read())
                except Exception as e:
                    print(e)
                    print("ダウンロード 失敗 ... [%s]" % os.path.basename(resource))
                    msg = msg + "ダウンロード 失敗 ... [%s]" % os.path.basename(resource) + "\n"
                finally:
                    time.sleep(3)
        else:
            msg = "取得できる画像がありません。"
            return msg

        msg = msg + "画像のクローリング処理が終了しました。" + "\n" + dwFilePath
        return msg

    @staticmethod
    def get_html_string(url):
        """
            Content:
                HTML取得
            Param:
                url    HTMLを取得するURL
        """
        decoded_html = ""

        # HTMLを取得
        try:
            request = urllib.request.urlopen(url)
            html = request.read()
        except:
            return decoded_html

        # エンコードを取得
        enc = WebCrawlerLogic.check_encoding(html)
        if enc == None:
            return decoded_html

        # HTMLをデコード
        decoded_html = html.decode(enc)

        return decoded_html

    @staticmethod
    def check_encoding(byte_string):
        """
            Content:
                文字コード確認
            Param:
                byte_string: バイト文字列
        """
        encoding_list = ["utf-8", "utf_8", "euc_jp",
                        "euc_jis_2004", "euc_jisx0213", "shift_jis",
                        "shift_jis_2004","shift_jisx0213", "iso2022jp",
                         "iso2022_jp_1", "iso2022_jp_2", "iso2022_jp_3",
                        "iso2022_jp_ext","latin_1", "ascii"]

        for enc in encoding_list:
            try:
                byte_string.decode(enc)
                break
            except:
                enc = None

        return enc
