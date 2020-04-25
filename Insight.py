from itertools import product
# from insight_helper.py import EnumerateInsight

aggs = ["SUM", "COUNT", "AVG", "MAX", "MIN"]
# normal_dims = ["aid", "vid", "type", "year", "coauthor"]
normal_dims = [0, 1, 2, 3, 4]
q4_dims = []
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


def get_all_ces(tau, dims):
    if tau == 1:
        return ["COUNT"]
    elif tau > 1:
        this_round = list(product(ce_index, dims))
        round_before = get_all_ces(tau-1, dims)
        return list(product(round_before, this_round))


def get_compatible_ces(tau, dims):
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


# print(len(get_all_ces(3)))
# print(len(get_compatible_ces(3)))

def insights(R, tau, k):
    H = []  # element (score, {"SG": SG, "Ce": ce, "type": T})

    dims = []
    if R == 1 or R == 2 or R == 3:
        dims = normal_dims
    elif R == 4:
        dims = q4_dims
    else:
        print("Illegal dataset index")

    O = get_compatible_ces(tau, dims)
    d = len(dims)
    for ce in O:
        for i in range(d):
            S = ['*', '*', '*', '*', '*']
            # EnumerateInsight(S, i, ce, H, R, k)
    return H


print(get_all_ces(2, normal_dims))