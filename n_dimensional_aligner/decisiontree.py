# @author: Ronald Haentjens Dekker


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
    def __init__(self):
        self.coordinates = (0, 0, 0)
    pass


class DecisionTree(object):

    def __init__(self, witnesses):
        self.witnesses = witnesses
        self.root = DecisionNode()

    pass