import logging
import os

from PIL import Image
from django.conf import settings
from keras.layers import Activation, Dense, Dropout
from keras.models import Sequential
from keras.models import model_from_json
from keras.optimizers import Adagrad
from keras.optimizers import Adam
from keras.utils.np_utils import to_categorical

from MlApp.models.mstimagelabel import Mst_imagelabel
import numpy as np


# ログ変数
logger = logging.getLogger('command')

# 学習ファイル定義名
modelFilePath = '/data/model/mlapp_model.json'
h5File = 'mlapp_model_weights.h5'

class ImagelearnLogic:

    # データ学習処理
    def imageleanExec(self):

        try:
            # フォームからフォルダパスを取得
            TRAIN_DIR = self.data['dataFolder']
            # settingsからMLAPPのパスを取得
            MLAPP_DIR = getattr(settings, 'MLAPP_DIR', None);
            # データラベル取得
            dataLabelCd = self.data['category_1'] + self.data['category_2'] + self.data['category_3']
            if len(dataLabelCd) < 9:
                return "ラベルが正しく設定されていません。"

            # 学習用のデータを作る.
            image_list = []
            label_list = []
            dir_list = []

            # ディレクトリが存在しない場合はエラー
            dir_list = os.listdir(TRAIN_DIR)
            if not dir_list or len(dir_list)==0:
                return "訓練データフォルダまたはファイルがありません。"

                # 指定したフォルダ以下の画像を読み込む。
                for dir in os.listdir(TRAIN_DIR):

                    dir1 = TRAIN_DIR + dir
                    label = dataLabelCd

                    for file in os.listdir(dir1):
                        # 配列label_listに正解ラベルを追加(DBから取得した対象の連結コード)
                        label_list.append(label)
                        filepath = dir1 + "/" + file
                        # 画像を25x25pixelに変換し、1要素が[R,G,B]3要素を含む配列の25x25の２次元配列として読み込む。
                        # [R,G,B]はそれぞれが0-255の配列。
                        image = np.array(Image.open(filepath).resize((25, 25)))
                        print(filepath)
                        # 配列を変換し、[[Redの配列],[Greenの配列],[Blueの配列]] のような形にする。
                        image = image.transpose(2, 0, 1)
                        # さらにフラットな1次元配列に変換。最初の1/3はRed、次がGreenの、最後がBlueの要素がフラットに並ぶ。
                        image = image.reshape(1, image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]
                        # 出来上がった配列をimage_listに追加。
                        image_list.append(image / 255.)

                # kerasに渡すためにnumpy配列に変換。
                image_list = np.array(image_list)

                # ラベルの配列を1と0からなるラベル配列に変更
                # 0 -> [1,0], 1 -> [0,1] という感じ。
                Y = to_categorical(label_list)

                # モデルを生成してニューラルネットを構築
                model = Sequential()
                model.add(Dense(200, input_dim=1875))
                model.add(Activation("relu"))
                model.add(Dropout(0.2))

                model.add(Dense(200))
                model.add(Activation("relu"))
                model.add(Dropout(0.2))

                model.add(Dense(2))
                model.add(Activation("softmax"))

                # オプティマイザにAdamを使用
                opt = Adam(lr=0.001)
                # モデルをコンパイル
                model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=["accuracy"])
                # 学習を実行。10%はテストに使用。
                model.fit(image_list, Y, nb_epoch=1500, batch_size=100, validation_split=0.1)

                # 学習結果を保存。
                model_json_str = model.to_json()
                mlapp_model_fileName = MLAPP_DIR + modelFilePath
                open(mlapp_model_fileName, 'w').write(model_json_str)
                model.save_weights(h5File);

                return "学習処理を実行しました。"

        except FileNotFoundError:
                            return "訓練データフォルダまたはファイルがありません。"
        except NotADirectoryError:
                            return "訓練データフォルダまたはファイルがありません。"


    # データ判定
    def imageJudgmentExec(self):

        try:
            # フォームからフォルダパスを取得
            dataFolder = self.data['dataFolder']
            testFile = self.data['testFile']

            # settingsからMLAPPのパスを取得
            MLAPP_DIR = getattr(settings, 'MLAPP_DIR', None);

            # 学習用のデータを作る.
            label_list = []
            dir_list = []

            # モデルを読み込む
            model = Sequential()
            mlapp_model_fileName = MLAPP_DIR + modelFilePath

            model = model_from_json(open(mlapp_model_fileName).read())
            # 学習結果を読み込む
            model.load_weights(h5File)

            # ファイルが指定されている場合はファイルの判定となり、ファイル指定がない場合はフォルダ単位の判定
            if testFile is not None :
                # 画像データ数値置き換えと判定
                image = np.array(Image.open(testFile).resize((25, 25)))
                image = image.transpose(2, 0, 1)
                image = image.reshape(1, image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]
                result = model.predict_classes(np.array([image / 255.]))

                # ラベルコードによる表示名称取得
                dataLabelCd = result[0]
                labelclass1 = dataLabelCd[0,3]
                labelclass2 = dataLabelCd[3,3]
                labelclass3 = dataLabelCd[8,3]

                # イメージラベルオブジェクト
                imagelabel_name1 = ''
                imagelabel_name2 = ''
                imagelabel_name3 = ''

                for objimagelabel in Mst_imagelabel.objects.filter(labelclass=labelclass1):
                    imagelabel_name1 = objimagelabel.labelclassname

                for objimagelabel in Mst_imagelabel.objects.filter(labelclass=labelclass2):
                    imagelabel_name2 = objimagelabel.labelclassname

                for objimagelabel in Mst_imagelabel.objects.filter(labelclass=labelclass3):
                    imagelabel_name3 = objimagelabel.labelclassname

                return ("データ判定結果: ", imagelabel_name1 + " ", imagelabel_name2 + " ", imagelabel_name3)

            else :
                # ディレクトリが存在しない場合はエラー
                dir_list = os.listdir(dataFolder)
                if not dir_list or len(dir_list)==0:
                    return "判定データフォルダがありません。"

                    # フォルダの画像でチェック。ラベルに対する正解を表示する。
                    total = 0.
                    ok_count = 0.

                    # データラベル取得
                    dataLabelCd = self.data['category_1'] + self.data['category_2'] + self.data['category_3']

                    for dir in os.listdir(dataFolder):

                        dir1 = MLAPP_DIR + dir

                        for file in os.listdir(dir1):
                            label_list.append(dataLabelCd)
                            filepath = dir1 + "/" + file
                            image = np.array(Image.open(filepath).resize((25, 25)))
                            print(filepath)
                            image = image.transpose(2, 0, 1)
                            image = image.reshape(1, image.shape[0] * image.shape[1] * image.shape[2]).astype("float32")[0]
                            result = model.predict_classes(np.array([image / 255.]))
                            print("label:", dataLabelCd, "result:", result[0])

                            total += 1.

                            if dataLabelCd == result[0]:
                                ok_count += 1.

                    return ("データ判定の正解率: ", ok_count / total * 100, "%")

        except FileNotFoundError:
                            return "判定データフォルダまたはファイルがありません。"
        except NotADirectoryError:
                            return "判定データフォルダまたはファイルがありません。"


    # 学習データ削除
    def imageModelDeleteExec(self):

        try:
            # settingsからMLAPPのパスを取得
            MLAPP_DIR = getattr(settings, 'MLAPP_DIR', None);
            # 学習データの削除
            mlapp_model_fileName = MLAPP_DIR + modelFilePath
            os.remove(mlapp_model_fileName)
            return "学習データを削除しました。"

        except FileNotFoundError:
                            return "判定データフォルダまたはファイルがありません。"
