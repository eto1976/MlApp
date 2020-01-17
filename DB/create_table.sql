/* ���[�U�[�e�[�u�� */
CREATE TABLE mst_user (
    id VARCHAR(5) -- ���[�U�[ID
  , name VARCHAR(20) NOT NULL -- ���[�U�[��
  , password VARCHAR(20) NOT NULL -- �p�X���[�h
  , mailAddress VARCHAR(40) -- ���[���A�h���X
  , adminFlg CHAR(1) -- �Ǘ��҃t���O
  , createDate DATE -- �쐬����
  , updateDate DATE -- �ŏI�X�V����
  , PRIMARY KEY (id)
  , UNIQUE (mailAddress)
);
/* �w�K�f�[�^ */
CREATE TABLE trn_learningdata (
    code VARCHAR(6) -- �f�[�^�R�[�h
  , type VARCHAR(2) -- �f�[�^���
  , folderPath VARCHAR(258) -- �t�H���_�p�X
  , lnModelNm VARCHAR(100) -- �w�K���f����
  , createDate DATE -- �쐬����
  , updateDate DATE -- �ŏI�X�V����
  , PRIMARY KEY (code)
);
/* �摜���x���}�X�^ */
CREATE TABLE mst_imageLabel (
    labelClass1 VARCHAR(3) -- ���x���N���X1
  , labelClass1Name VARCHAR(100) -- ���x���N���X1����
  , labelClass2 VARCHAR(3) -- ���x���N���X2
  , labelClass2Name VARCHAR(100) -- ���x���N���X2����
  , labelClass3 VARCHAR(3) -- ���x���N���X3
  , labelClass3Name VARCHAR(100) -- ���x���N���X3����
  , PRIMARY KEY (labelClass1)
  , UNIQUE (labelClass2, labelClass3)
);
