# @author: Ronald Haentjens Dekker
from collatex.tokenindex import TokenIndex


def calculate_maximum(lcp_intervals):
    # calculate maximum avout matches
    # for now we forget that once things are matched
    # this does not yet work for repetitions etc
    # for interval in lcp_intervals:
    #    print(interval)

    possible_matches = 0
    for interval in lcp_intervals:
        possible_matches += interval.number_of_witnesses
    return possible_matches


class DecisionNode(object):
    def __init__(self, global_maximum_score):
        self.coordinates = (0, 0, 0)
        self.current_score = 0
        self.minimum_global_score = 0
        self.maximum_global_score = global_maximum_score
    pass


class DecisionTree(object):

    def __init__(self, witnesses):
        self.witnesses = witnesses
        self.tokenindex = TokenIndex(witnesses)
        self.tokenindex.prepare()
        self.lcp_intervals = self.tokenindex.split_lcp_array_into_intervals()
        global_maximum_score = calculate_maximum(self.lcp_intervals)
        self.root = DecisionNode(global_maximum_score)

    pass