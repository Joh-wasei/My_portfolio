from django.shortcuts import render
from django.views.generic import View
from .models import Profile, Work
# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        profile_data = Profile.objects.all() #全てのprofileデータを取得
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0] #降順に並べ替え、最新のprofileデータを取得
        work_data = Work.objects.order_by('-id')
        return render(request, 'app/index.html', {
            'profile_data': profile_data,
            'work_data': work_data,
        })