from django import forms

from .models import Variation


class VariationInventoryForm(forms.ModelForm):
	class Meta:
		model = Variation
		fields = ('title', 'price', 'sale_price', 'inventory', 'active')


VariationInventoryFormSet = forms.models.modelformset_factory(Variation, form=VariationInventoryForm, extra=1)