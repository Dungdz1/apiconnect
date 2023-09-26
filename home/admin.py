from django.contrib import admin
from .models import SinhVien, Lop

# Register your models here.

class SinhVienAdmin(admin.ModelAdmin):
    list_display = ('masv', 'hotensv', 'lophocphan', 'ngaysinh', 'ghichu')
    search_fields = ('masv', 'hotensv', 'lophocphan')
admin.site.register(SinhVien, SinhVienAdmin)

class LopAdmin(admin.ModelAdmin):
    list_display = ('lophocphan', 'gvcn', 'hotensv')
    search_fields = ('lophocphan', 'gvcn', 'hotensv')
admin.site.register(Lop, LopAdmin)