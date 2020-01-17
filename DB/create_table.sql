/* ユーザーテーブル */
CREATE TABLE mst_user (
    id VARCHAR(5) -- ユーザーID
  , name VARCHAR(20) NOT NULL -- ユーザー名
  , password VARCHAR(20) NOT NULL -- パスワード
  , mailAddress VARCHAR(40) -- メールアドレス
  , adminFlg CHAR(1) -- 管理者フラグ
  , createDate DATE -- 作成日時
  , updateDate DATE -- 最終更新日時
  , PRIMARY KEY (id)
  , UNIQUE (mailAddress)
);
/* 学習データ */
CREATE TABLE trn_learningdata (
    code VARCHAR(6) -- データコード
  , type VARCHAR(2) -- データ種別
  , folderPath VARCHAR(258) -- フォルダパス
  , lnModelNm VARCHAR(100) -- 学習モデル名
  , createDate DATE -- 作成日時
  , updateDate DATE -- 最終更新日時
  , PRIMARY KEY (code)
);
/* 画像ラベルマスタ */
CREATE TABLE mst_imageLabel (
    labelClass1 VARCHAR(3) -- ラベルクラス1
  , labelClass1Name VARCHAR(100) -- ラベルクラス1名称
  , labelClass2 VARCHAR(3) -- ラベルクラス2
  , labelClass2Name VARCHAR(100) -- ラベルクラス2名称
  , labelClass3 VARCHAR(3) -- ラベルクラス3
  , labelClass3Name VARCHAR(100) -- ラベルクラス3名称
  , PRIMARY KEY (labelClass1)
  , UNIQUE (labelClass2, labelClass3)
);
