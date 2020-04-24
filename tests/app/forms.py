from django import forms


class TestForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100, help_text="Your full name")
    age = forms.IntegerField(label="Age", help_text="An educated guess will do")
    gender = forms.ChoiceField(label="Gender", choices=(("F", "she/her"), ("M", "he/him")))
    drink = forms.ChoiceField(
        label="Drink",
        choices=(("water", "water"), ("juice", "juice",), ("tea", "tea"), ("coffee", "coffee")),
        widget=forms.RadioSelect,
    )
    food = forms.MultipleChoiceField(
        label="Food",
        choices=(("pizza", "pizza"), ("veggie bowl", "veggie bowl",), ("falafel", "falafel")),
        help_text="All of our products are vegetarian",
    )
    dessert = forms.MultipleChoiceField(
        label="Dessert",
        choices=(("ice cream", "ice cream"), ("pancakes", "pancakes")),
        widget=forms.CheckboxSelectMultiple,
    )

    def clean(self):
        result = super().clean()
        raise forms.ValidationError("Houston, we have a problem.")
        return result
