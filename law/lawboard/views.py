from django.shortcuts import render,redirect
from .models import *
from django.utils import timezone

def lawboardList(request):
    lawboards= LawBoard.objects.all()
    return render(request, 'lawboard_list.html', {'lawboards': lawboards})

def lawboardNew(request):
    return render(request, 'lawboard_new.html')

def lawboardCreate(request):
    new_lb = LawBoard()
    new_lb.title = request.POST['title']
    new_lb.pub_date = timezone.datetime.now()
    new_lb.writer = request.user
    new_lb.body = request.POST['body']
    new_lb.save()

    return redirect('lb_list')

def lawboardEdit(request, lb_id):
    edit_lb = LawBoard.objects.get(id = lb_id)
    return render(request,'lawboard_edit.html',{'lb': edit_lb})

def lawboardUpdate(request, lb_id):
    update_lb = LawBoard.objects.get(id = lb_id)
    update_lb.title = request.POST['title']
    update_lb.body = request.POST['body']
    update_lb.save()
    return redirect('lb_list')

def lawboardDetail(request, lb_id):
    detail_lb = LawBoard.objects.get(id=lb_id)
    return render(request, 'lawboard_detail.html',{'lb':detail_lb})

def lawboardDelete(request, lb_id):
    delete_lb = LawBoard.objects.get(id=lb_id)
    delete_lb.delete()
    return redirect('lb_list')

def meetingboardList(request):
    meetingboards= MeetingBoard.objects.all()
    return render(request, 'Meetingboard_list.html', {'meetingboards': meetingboards})

def meetingboardNew(request):
    return render(request, 'meetingboard_new.html')

def meetingboardCreate(request):
    new_mb = MeetingBoard()
    new_mb.title = request.POST['title']
    new_mb.pub_date = timezone.datetime.now()
    new_mb.writer = request.user
    new_mb.body = request.POST['body']
    new_mb.save()

    return redirect('mb_list')

def meetingboardEdit(request, mb_id):
    edit_mb = MeetingBoard.objects.get(id = mb_id)
    return render(request,'meetingboard_edit.html',{'mb': edit_mb})

def meetingboardUpdate(request, mb_id):
    update_mb = MeetingBoard.objects.get(id = mb_id)
    update_mb.title = request.POST['title']
    update_mb.body = request.POST['body']
    update_mb.save()
    return redirect('mb_list')

def meetingboardDetail(request, lb_id):
    detail_mb = MeetingBoard.objects.get(id=mb_id)
    return render(request, 'meetingboard_detail.html',{'lb':detail_mb})

def meetingboardDelete(request, lb_id):
    delete_mb = MeetingBoard.objects.get(id=mb_id)
    delete_mb.delete()
    return redirect('mb_list')





