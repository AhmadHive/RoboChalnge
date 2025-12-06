# views.py
from django.shortcuts import render
from django.http import HttpResponse
import os
from django.conf import settings

def information(request):
    return render(request, 'information.html')

def download_challenge_file(request):
    try:
    
        file_path = os.path.join(settings.STATIC_ROOT, 'files', 'robotics_challenge.docx')

        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(
                    file.read(),
                    content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                )
                response['Content-Disposition'] = 'attachment; filename="robotics_challenge.docx"'
                return response
        else:
            return HttpResponse(
                "الملف غير موجود. تأكد من أن الملف في static/files/robotics_challenge.docx"
            )
    except Exception as e:
        return HttpResponse(f"حدث خطأ أثناء التحميل: {str(e)}")
