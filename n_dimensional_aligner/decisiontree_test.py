from unittest import TestCase

from collatex.core_classes import Witness

# @author: Ronald Haentjens Dekker
# we first build the decision tree constructs
from collatex.tokenindex import TokenIndex

from n_dimensional_aligner.decisiontree import calculate_maximum


class DecisionTreeTest(TestCase):

    def test_maximum_score(self):
        # we need to create witnesses
        # 1: a, b, c, d, e
        # 2: a, e, c, d
        # 3: a, d, b

        a = Witness({'id':'A', 'content':"a b c d e"})
        b = Witness({'id':'B', 'content':"a e c d"})
        c = Witness({'id':'C', 'content':"a d b"})

        witnesses = [a, b, c]
        tokenindex = TokenIndex(witnesses)
        tokenindex.prepare()

        # from the token index we need to calculate the maximum amount of matches
        lcp_intervals = tokenindex.split_lcp_array_into_intervals()
        possible_matches = calculate_maximum(lcp_intervals)

        # print(possible_matches)
        self.assertEquals(12, possible_matches)

