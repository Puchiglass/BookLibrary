from django.test import TestCase

from library.forms import RegisterUserForm

class RegisterUserFormTest(TestCase):
    def test_register_form_date_field_label(self):
        form = RegisterUserForm()
        self.assertTrue(
            form.fields['email'].label is None or 
            form.fields['email'].label == 'Адрес электронной почты'
        )