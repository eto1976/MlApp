from django.db import models

# Create your models here.
class Mst_imagelabel(models.Model):
    """
    MstImagelabel to do.
    """
    labelclass = models.CharField(primary_key=True,max_length=3)
    labelclassname = models.CharField(max_length=100)
    baselabelclass = models.CharField(max_length=3)

    class Meta:
            managed = False
            db_table = 'mst_imagelabel' # 使用テーブル

    def __str__(self):
        return self.labelclass