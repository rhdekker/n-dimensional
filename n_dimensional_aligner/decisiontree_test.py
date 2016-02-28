from unittest import TestCase

from collatex.core_classes import Witness

# @author: Ronald Haentjens Dekker
# we first build the decision tree constructs
from collatex.tokenindex import TokenIndex

from n_dimensional_aligner.decisiontree import calculate_maximum, DecisionTree


class DecisionTreeTest(TestCase):

    def setUp(self):
        # we need to create witnesses
        # 1: a, b, c, d, e
        # 2: a, e, c, d
        # 3: a, d, b

        a = Witness({'id':'A', 'content':"a b c d e"})
        b = Witness({'id':'B', 'content':"a e c d"})
        c = Witness({'id':'C', 'content':"a d b"})

        self.witnesses = [a, b, c]
        self.tokenindex = TokenIndex(self.witnesses)
        self.tokenindex.prepare()

    def test_maximum_score(self):
        # from the token index we need to calculate the maximum amount of matches
        lcp_intervals = self.tokenindex.split_lcp_array_into_intervals()
        possible_matches = calculate_maximum(lcp_intervals)

        # print(possible_matches)
        self.assertEquals(12, possible_matches)

    def test_decision_tree(self):
        tree = DecisionTree(self.witnesses)
        root = tree.root
        self.assertEquals((0, 0, 0), root.coordinates)
        # we need three scores, (current score), (minimum global score, maximum global score)
        self.assertEquals(0, root.current_score)
        self.assertEquals(0, root.minimum_global_score)
        self.assertEquals(12, root.maximum_global_score)
        # we need to keep track of the open options..
        # we have the unexpanded ones, and the expanded ones..
        # type of edit operation (attempt to match or to skip) and witness number the node represents (1, 2, 3)
        # self.assertEquals()


#    def



