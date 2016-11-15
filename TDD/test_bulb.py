import unittest
from bulb_classes import LightBulb, LightBulbFactory

class LightBulbTest(unittest.TestCase):

    def setUp(self):
        # using this method to create an instance of the bulb factory, adding new light bulb
        self.bulb_factory = LightBulbFactory()
        self.bulb = self.bulb_factory.create_bulb("GE")

        def testNewBulbIsLightBulb(self):
            # is this indeed a light bulb??
            return self.assertIsInstance(self.bulb, LightBulb)

        def testNewBulbHasBrand(self):
            # testing for brand
            return self.assertEqual("GE", self.bulb.brand)

        def testBulbDefaultOff(self):
        # testing off by default
            return self.assertEqual(False, self.bulb.on_or_off())

        def testTurnOnBulb(self):
            self.bulb.switch_on()
            return self.assertEqual(True, self.bulb.on_or_off())
if __name__ == '__main__':
    unittest.main()
