
import unittest
from custom_functions import temperature_methods

narigno = [15, 14, 16, 12, 14, 16, 13, 14, 12, 10, 16, 17]

class TestCollectionMethods(unittest.TestCase):

    def test_average(self):
        guajira = [35, 30, 25, 32, 29, 29, 36, 35, 28, 37, 38, 30]
        guajira_average = temperature_methods.average(guajira)

        self.assertEqual(guajira_average, 31)


    def test_average2(self):
        santander = [18, 25, 20, 24, 23, 24, 21, 23, 29, 21, 23, 25]
        santander_average = temperature_methods.average(santander)

        self.assertEqual(santander_average, 23)






