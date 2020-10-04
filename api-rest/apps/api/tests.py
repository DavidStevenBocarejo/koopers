from django.test import TestCase
import unittest

#Models
#from ..core.models import *
#from .models import *
#from api-rest.apps.core.models import Category
#from ..apps.core.models import Category
#from apps.core.models import Category

# Create your tests here.
class TestStringMethods(unittest.TestCase):

    def setUp(self):
        Category.objects.create(
            title='Test de prueva',
        )
    
    def Test_category_exist(self):
        test_categry = Category.objects.filter(title='Test de prueva').exist()
        self.assertEqual(test_categry, True)


if __name__ == '__main__':
    unittest.main()