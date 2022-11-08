import imp
from multiprocessing import context
from operator import imod
import re
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from sotuken.forms import KakikomiForm
from . import forms
from . forms import KakikomiForm

def kakikomi(request):
    paramas = {
        '基礎代謝':'基礎代謝',
        'f':KakikomiForm(),
        'TDEE':'TDEE',
        '総消費カロリー':'総消費カロリー',
        '目標カロリー':'目標カロリー',
        'BMI':'BMI',
        '減量目標':'減量目標',
    }
    if request.method == 'POST':
        if (float(request.POST['性別']) == 0.5473):
            hp1 = 66.47
            hp2 = 13.75
            hp3 = 5
            hp4 = 6.76
        else:
            hp1 = 655.1
            hp2 = 9.56
            hp3 = 1.85
            hp4 = 4.68
        paramas['基礎代謝']=hp1 + hp2 *float(request.POST['体重']) + hp3 *float(request.POST['身長']) - hp4 * float(request.POST['年齢'])
        paramas['TDEE']=float(request.POST['運動'])
        paramas['f'] = KakikomiForm(request.POST)
        paramas['総消費カロリー']=float(paramas['TDEE']*paramas['基礎代謝'])
        paramas['BMI']=float(request.POST['体重'])/float(int(request.POST['身長'])*int(request.POST['身長']) / 10000)
        if (float(paramas['BMI']) >= 35):
            mp = 0.05
        else:
            mp = 0.03
        paramas['減量目標']= mp*float(request.POST['体重'])
        paramas['目標カロリー']=paramas['総消費カロリー'] - (paramas['減量目標']*7000/90)
        paramas['朝']=paramas['目標カロリー']*0.3
        paramas['昼']=paramas['目標カロリー']*0.3
        paramas['晩']=paramas['目標カロリー']*0.4
        paramas['朝P']=paramas['朝']*0.2/4
        paramas['朝F']=paramas['朝']*0.2/9
        paramas['朝C']=paramas['朝']*0.6/4
        paramas['昼P']=paramas['昼']*0.2/4
        paramas['昼F']=paramas['昼']*0.2/9
        paramas['昼C']=paramas['昼']*0.6/4
        paramas['晩P']=paramas['晩']*0.2/4
        paramas['晩F']=paramas['晩']*0.2/9
        paramas['晩C']=paramas['晩']*0.6/4

        
    return render(request, 'sotuken/KakikomiForm.html',paramas)
class SampleChoiceView(View):
    def get(self,request):
        form = forms.SampleChoiceForm()
        context = {
            'form': form
        }
        return render(request, 'sotuken/KakikomiForm.html',context)
        sample_choice_view = SampleChoiceView.as_view()