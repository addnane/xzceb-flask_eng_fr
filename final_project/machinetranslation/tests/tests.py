
""" this module is to test the translation function imported from the translator.py"""
import unittest
from translator import englishtofrench,frenchtoenglish
class TestTranslate(unittest.TestCase):
    """Create a testing class that inherits from unittest.testcase"""
    def testenglishtofrench(self):
        """test the function english to french"""
        self.assertRaises(Exception,"")
        self.assertEqual(englishtofrench("Book")["translations"][0]["translation"],"Livre")
        self.assertNotEqual(englishtofrench("White")["translations"][0]["translation"],"Noir")
        self.assertEqual(englishtofrench("Hello")["translations"][0]["translation"],"Bonjour")

    
    def testfrenchtoenglish(self):
        """test the function french to english"""
        self.assertRaises(Exception,"")
        self.assertEqual(frenchtoenglish("Livre")["translations"][0]["translation"],"Book")
        self.assertNotEqual(frenchtoenglish("Blanc")["translations"][0]["translation"],"Black")
        self.assertEqual(frenchtoenglish("Bonjour")["translations"][0]["translation"],"Hello")



if __name__ == "__main__":
    unittest.main()

