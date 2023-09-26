from django.db import models

# Create your models here.
class SinhVien(models.Model):
    masv = models.CharField(max_length=10, primary_key=True)
    hotensv = models.CharField(max_length=30, blank=False, null=False)
    lophocphan = models.CharField(max_length=10, blank=False, null=False)
    ngaysinh = models.DateField(blank=False, null=False)
    ghichu = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.hotensv


class Lop(models.Model):
    lophocphan = models.CharField(max_length=10, blank=False, null=True)
    #lophocphan = models.CharField(max_length=10)
    gvcn = models.CharField(max_length=30, primary_key=True)
    hotensv = models.CharField(max_length=30)

    def __str__(self):
        return self.lophocphan