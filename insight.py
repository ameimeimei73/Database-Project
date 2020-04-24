from heapq import heappush, heappop
from itertools import product

H = []  # element (score, {"SG": SG, "Ce": ce, "type": T})
aggs = ["SUM", "COUNT", "AVG", "MAX", "MIN"]
dims = ["aid", "vid", "year", "type", "coauthor"]
ce_index = [0, 1, 2, 3, 4, 5, 6, 7]
###############   rank    %    davg  dprev  avg   min   max     sum
compatible_ce = [[True, False, True, True, False, False, False, False],    # rank
                 [True, False, True, True, False, True, True, False],      # %
                 [True, False, True, True, False, True, True, False],      # davg
                 [True, False, True, True, True, True, True, False],       # dprev
                 [True, False, False, True, True, True, True, False],      # avg
                 [False, False, True, True, True, False, False, False],    # min
                 [False, False, True, True, True, False, False, False],    # max
                 [True, False, True, True, False, True, True, False]]      # sum

def extractors(index, data):
    if index == 0:
        # rank
        pass
    elif index == 1:
        # percent
        pass
    elif index == 2:
        # delta_avg
        pass
    elif index == 3:
        # delta_prev
        pass
    elif index == 4:
        # avg
        pass
    elif index == 5:
        # min
        pass
    elif index == 6:
        # max
        pass
    elif index == 7:
        # sum
        pass


def get_all_ces(tau):
    if tau == 1:
        return ["COUNT"]
    elif tau > 1:
        this_round = list(product(ce_index, dims))
        round_before = get_all_ces(tau-1)
        return list(product(round_before, this_round))


def get_compatible_ces(tau):
    if tau == 1 or tau == 2:
        return get_all_ces(tau)
    elif tau > 2:
        res = []
        all_ces = get_all_ces(tau)
        for item in all_ces:
            new_item = []

            while len(item) > 1 and type(item) != type('COUNT'):  # remove nested tuples from product operation
                new_item.append(item[1])
                item = item[0]
            new_item.append(item)

            new_item.reverse()
            compatible = True
            for i in range(1, len(new_item) - 1):
                op1 = new_item[i][0]
                op2 = new_item[i+1][0]
                if compatible_ce[op1][op2] == False:
                    compatible = False
                    break

            if compatible:
                res.append(new_item)

        return res


print(len(get_all_ces(3)))
print(len(get_compatible_ces(3)))
