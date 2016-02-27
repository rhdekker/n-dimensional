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
