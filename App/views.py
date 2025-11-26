from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import os
from django.conf import settings

def information(request):
    return render(request, 'information.html')

def download_challenge_file(request):
    try:
        # المسار الصحيح بعد تعديل الاسم
        file_path = os.path.join(settings.BASE_DIR, 'static', 'files', 'robotics_challenge.docx')
        
        print(f"جاري تحميل الملف من: {file_path}")  # للتصحيح
        print(f"الملف موجود: {os.path.exists(file_path)}")  # للتصحيح
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), 
                    content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
                response['Content-Disposition'] = 'attachment; filename="robotics_challenge.docx"'
                return response
        else:
            return HttpResponse("الملف غير موجود. تأكد من أن الملف في static/files/robotics_challenge.docx")
            
    except Exception as e:
        return HttpResponse(f"حدث خطأ أثناء التحميل: {str(e)}")