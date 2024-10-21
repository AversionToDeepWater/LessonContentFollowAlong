from unittest import TestCase
from cylindervol import cylinder_volume

class TestCylinderVolume(TestCase):
    def test_correct_vol(self):
        result = cylinder_volume(3,4)
        self.assertEqual(result,113.09733552923255)

    def test_negative_radius(self):
        result = cylinder_volume(-3,4)
        self.assertEqual(result, None)

    def test_negative_water_height(self):
        result = cylinder_volume(3, -4)
        self.assertEqual(result, None)

    def test_only_numbers(self):
        result = cylinder_volume("string", "string")
        self.assertEqual(result, None)

    def test_zero(self):
        result = cylinder_volume(0,4)
        self.assertEqual(result,0)

    def test_tiny(self):
        result = cylinder_volume(0.03,0.04)
        self.assertEqual(result,0.00011309733552923255)



    pass


