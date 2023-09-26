from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SinhVien, Lop
from .serializers import SinhVienSerializer, LopSerializer
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST'])
def sinhvien_list(request):
    if request.method == 'GET':
        sinhvien = SinhVien.objects.all()
        serializer = SinhVienSerializer(sinhvien, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SinhVienSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def sinhviendetail(request,pk):
    try:
        sinhvien = SinhVien.objects.get(pk=pk) # select * from SinhVien where masv = pk
    except SinhVien.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SinhVienSerializer(sinhvien)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SinhVienSerializer(sinhvien, data=request.data) # update SinhVien set tensv = tensv, ngaysinh = ngaysinh, gioitinh = gioitinh, diachi = diachi, malop = malop where masv = pk
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sinhvien.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#####################
@api_view(['GET', 'POST'])
def lop_list(request):
    if request.method == 'GET':
        lop = Lop.objects.all()
        serializer = LopSerializer(lop, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = LopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def lopdetail(request,pk):
    try:
        lop = Lop.objects.get(pk=pk) # select * from SinhVien where masv = pk
    except Lop.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = LopSerializer(lop)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = LopSerializer(lop, data=request.data) # update SinhVien set tensv = tensv, ngaysinh = ngaysinh, gioitinh = gioitinh, diachi = diachi, malop = malop where masv = pk
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        lop.delete()
        return Response(status=status.HTTP_204_NO_CONTENTS)