import unittest
import super_algos

class Testsuper_algos(unittest.TestCase):

    def test_find_min(self):
        """
            checks to see if the minimum number is found in a list and if the list is empty it returns -1
        """
        num = [24,49,65,17,38,52,75,82,100]
        self.assertEqual(super_algos.find_min(num),17)
        self.assertEqual(super_algos.find_min([]),-1)

    def test_sum_all(self):
        """
            Adds all the numbers in the list and if the list is empty is must returns -1 
        """
        num = [249,49,65,17,38,52,75,82,100]
        self.assertEqual(super_algos.sum_all(num),727)
        self.assertEqual(super_algos.sum_all([]),-1)

    def test_find_possible_strings(self):
        """
            Checks to see if it returns all the possible strings of length from the character set
        """
        self.assertEqual(super_algos.find_possible_strings(['c','d'],2), ['cc', 'cd', 'dc', 'dd'])
        self.assertEqual(super_algos.find_possible_strings(["x", "y"], 3), ["xxx", "xxy", "xyx", "xyy", "yxx", "yxy", "yyx", "yyy"])
        self.assertEqual(super_algos.find_possible_strings(['c','d'],1), ['c','d'])