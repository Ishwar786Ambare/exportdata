from django.shortcuts import render

import io
from django.http import HttpResponse
from django.views.generic import View
import xlsxwriter

from exportapp.models import ExportData


# def get_simple_table_data():  # Simulate a more complex table read.
#     data = ExportData.objects.all()
#     return data
# return [[1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]]


def MyView(request, *args, **kwargs):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    worksheet.write(1, 0, 'name')
    worksheet.write(1, 1, 'mobile')
    data = ExportData.objects.all()
    print(data)
    num = 2
    for new in data:
        worksheet.write(num, 0, new.name)
        worksheet.write(num, 1, new.number)
        num += 1
    workbook.close()
    output.seek(0)
    filename = 'django_simple.xlsx'
    response = HttpResponse(output, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    output.close()
    return response


def home(request):
    data = ExportData.objects.all()
    return render(request, 'home.html', {'data': data})
