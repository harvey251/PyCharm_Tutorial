from django.test import TestCase

# Create your tests here.
from fix_me.views.security import secure_function


class TestAwesome(TestCase):
    def test_secrete_function(self):
        # ToDo Debug
        data = secure_function()
        print(data)
        assert "456" == data

    def test_names(self):
