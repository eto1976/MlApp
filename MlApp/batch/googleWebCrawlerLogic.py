import logging
import os
import ssl
import urllib.request
import re
import zipfile
from lxml import html

from django.conf import settings

context = ssl.create_default_context()

# ログ変数(環境に変更があった場合は修正)
logger = logging.getLogger('command')
# ChromeWebDriverのパス
driverFilePath = getattr(settings, "DRIVER_DIR", None)
# Chrome driver URL
chromeDriverUrl = "https://chromedriver.chromium.org/downloads"
# Chrome driver URL
chromeDriverStorageUrl = "https://chromedriver.storage.googleapis.com/"
# Chrome driver FileName
chromeDriverFileName = "/chromedriver_win32.zip"
# Chrome ApplicationFolder Path
chromePath = "C:/Program Files (x86)/Google/Chrome/Application"
# temp Directory
tempDirectory = "C:/temp"
# Use Proxy Flag
useProxy = "false"
# httpProxy
httpProxy = ""
# httpsProxy
httpsProxy = ""

class GoogleWebCrawlerLogic:

    """Auto update web driver
    getDriver.upCheckChromeDriver()
    """
    def upCheckChromeDriver(self) :
        """check chromeDriver Version
        """
        msg = ""
        #ローカルのChormeバージョン取得
        localversion = self.checkLocalChromeVersion()

        fna = self.checkLatestChromeDriverVersion(localversion)
        if fna == 0 :
            logger.info("対象バージョンのChromeWebDriver取得エラー")
            msg = "ChromeWebDriverが取得できません。"
            return msg
        furl = chromeDriverStorageUrl + fna + chromeDriverFileName
        urllib.request.urlretrieve(furl, tempDirectory + "/howa1.zip")
        with zipfile.ZipFile(tempDirectory + '/howa1.zip') as zipF:
            zipF.extractall(driverFilePath)

        majorVersion = re.search('^[0-9]*', fna)
        #比較用のローカルクロームのバージョン保持　後でどこかにセット
        localChromeDVersion = majorVersion.group()
        logger.info("ChromeWebDriverローカルバージョン = " + localChromeDVersion )
        msg = "ChromeWebDriverの更新が正常に終了しました。\n" + "ChromeWebDriverVersion = " + localChromeDVersion
        return msg

    # upCheckChromeDriverの内部メソッド
    # ローカルのChromeDriverのバージョン取得
    def checkLocalChromeVersion(self) :
        """
        check Chrome Version (for Windows) check local Chrome Browser Version
        """
        # get CromeApplicationFolderTree
        files = os.listdir(chromePath)
        # Collect directories only
        filesDir = [f for f in files if os.path.isdir(os.path.join(chromePath, f))]

        # get lastest Version
        version = 0
        for folder in filesDir :
            # get Major Version
            filePattern = re.compile(r'([0-9]+(?=\.))')
            result = filePattern.match(folder)
            if result:
                version = max(version,int(result.group()))

        # can't get Chrome Version return 0
        return version


    # upCheckChromeDriverの内部メソッド
    # Web上のローカルのChromeDriverの対象バージョン取得
    def checkLatestChromeDriverVersion(self, localChromeVersion) :
        """get chromeDriver Address for match local chrome version
        """
        # if
        if useProxy == "true" :
            os.environ["http_proxy"] = httpProxy
            os.environ["https_proxy"] = httpsProxy

        url = chromeDriverUrl
        try:
            with urllib.request.urlopen(url) as f:
                htmltext = f.read().decode('utf-8')
        except Exception as e:
            print("urlopenError: "+e)
            logger.info("urlopenError: "+e)

        #debug
        #print(htmltext.replace('\xa0', ''))

        title = html.fromstring(htmltext).xpath("//table[@class='sites-layout-name-one-column sites-layout-hbox']/tbody//ul")
        # Full Path from 2019/11/20
        # //table[@class='sites-layout-name-one-column sites-layout-hbox']/tbody/tr/td/div/div/ul/li
        #
        # getLinkTitle
        #aaa = title[0].xpath("span")
        # getLing
        chromeDriverVersionList = title[0].xpath("li")

        mi = "0"
        for version in chromeDriverVersionList :
            ccc = version.xpath("a")
            # DriverVersionAll...............................
            if(len(ccc)==0):
                continue
            chromeDriverStatus = ccc[0].text
            m = re.search('(?<=ChromeDriver )[0-9]*', chromeDriverStatus)
            if(str(m.group()) == str(localChromeVersion)) :
                versionOfMajor = re.search('(?<=ChromeDriver ).*', chromeDriverStatus)
                mi = str(versionOfMajor.group())
        if mi == "0":
            # no match ////////////////////////////////////
            print("No Match Chrome Driver Version")
            return 0
        return mi

