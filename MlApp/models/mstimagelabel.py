from django.db import models

# Create your models here.
class Mst_imagelabel(models.Model):
    """
    MstImagelabel to do.
    """
    class Meta:
            db_table = 'mst_imagelabel' # 使用テーブル

    labelclass = models.CharField(max_length=3)
    labelclassname = models.CharField(max_length=100)
    baselabelclass = models.CharField(max_length=3)
