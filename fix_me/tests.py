from django.test import TestCase

# Create your tests here.
from PyCharm_Tutorial.settings import other_secret_function
from fix_me.views.security import secure_function


class TestAwesome(TestCase):
    def test_secrete_function(self):
        # ToDo Debug
        data = secure_function()
        print(data)
        assert "456" == data

    def test_names(self):
        # ToDo: Find function "other_secret_function"
        # ToDo Rename all harveys
        names = other_secret_function()
        for name in names:
            self.assertTrue("harvey" not in name.lower(),
                             msg=f"WHAT ARE YOU DOING HERE {name}" )
