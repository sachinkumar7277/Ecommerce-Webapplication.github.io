from django import forms
from.models import item

class itemForm(forms.ModelForm):
    class Meta:
        model= item
        fields= ["category","item_img","item_name","price","discount_price","special_offer","stock","available"]


