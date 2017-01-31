"""
Unit tests for kissanime
"""
import unittest
from kissanime.kissanime_dl import KissAnime


class KissAnimeTests(unittest.TestCase):
    """
    Tests
    """
    def test_get_ep_no(self):
        """
            re test for episode number extraction
        """
        title1 = "Naruto Shippuuden (Sub) Episode 112"
        title2 = "Naruto Shippuuden (Sub) Episode 086-087"
        self.assertEqual(KissAnime._get_ep_no(title1), ["112"])
        self.assertEqual(KissAnime._get_ep_no(title2), ["086","087"])

if __name__ == '__main__':
    unittest.main()
