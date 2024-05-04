from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import ImgInpaintModel
from django.utils import timezone
import uuid
import numpy as np
import os
import cv2


class IndexPage(View):
    def get(self, request):
        data = {}
        # Fetch all List of Image Works Wich are completed
        img_inpaint_objs = ImgInpaintModel.objects.all()
        data={}
        data["title"] = "IMG INPAINT WORKS"
        data["img_inpaint_objs"] = img_inpaint_objs
        return render(request, 'Pages/index.html', data)
    

class ProcessImg(View):
    def get(self, request):
        data = {}
        data["title"] = "Process Image"
        return render(request, 'Pages/process_img.html', data)
    
    def post(self, request):        
        name = request.POST.get('name')
        damagedImg = request.FILES.get('damagedImg')
        maskedImg = request.FILES.get('maskedImg')

        model = ImgInpaintModel(name = name, damaged_img = damagedImg, masked_img = maskedImg)
        model.save()

        dmgImg = cv2.imread(model.damaged_img.path)
        mskImg = cv2.imread(model.masked_img.path, 0)
        resultImg = cv2.inpaint(dmgImg, mskImg, 3, cv2.INPAINT_NS)

        filename = f"result-img-{timezone.now().strftime('%Y%m%d%H%M%S')}_{uuid.uuid4().hex[:6]}.png"
        unique_file_path = os.path.join("static", "img", "result_img", filename)
        cv2.imwrite(unique_file_path, resultImg)
        
        model.result_img = unique_file_path
        model.save()

        return redirect('view-result', model.id)
    

class ViewResult(View):
    def get(self, request, imgID):
        data = {}
        data["title"] = "View Result"
        imgObj = ImgInpaintModel.objects.get(id = imgID)
        data["imgObj"] = imgObj
        return render(request, 'Pages/view_result.html', data)