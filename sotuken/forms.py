import re
from django import forms

class KakikomiForm(forms.Form):
    性別 = forms.fields.ChoiceField(
        choices=(
            ('1.0946','女'),
            ('0.5473','男')
        ),
            required=True,
            widget=forms.widgets.Select
    )
    名前 = forms.CharField()
    身長 =forms.IntegerField()
    体重 = forms.IntegerField()
    年齢 = forms.IntegerField()
    運動 = forms.fields.ChoiceField(
        choices=(
            ('1.2','週にほとんど運動しない'),
            ('1.375','週に１～２回程度運動する'),
            ('1.55','週に３～５回運動する'),
            ('1.725','週に６～７回程度運動する'),
            ('1.9','一日に2回程度運動する')
        ),
            required=True,
            widget=forms.widgets.Select
    )
