from copy import deepcopy


def extractors(index, data):
    # rank
    if index == 0:
        rank_arr = []
        # put all data in array with index as the rank
        for elem in data:
            if len(rank_arr) == 0:
                rank_arr.append(elem)
            else:
                inserted = False
                for i in range(len(rank_arr)):
                    if elem[1] > rank_arr[i][1]:
                        rank_arr.insert(i, elem)
                        inserted = True
                        break

                if not inserted:
                    rank_arr.append(elem)

        ret = set()
        for i in range(len(rank_arr)):
            ret.add((rank_arr[i][0], i))

        return ret

    # percent
    elif index == 1:
        denom = 0
        for elem in data:
            denom += elem[1]

        ret = set()
        for elem in data:
            percent = round(elem[1] / denom * 100, 2)
            ret.add((elem[0], percent))
        return ret

    # delta_avg
    elif index == 2:
        all_sum = 0
        for elem in data:
            all_sum += elem[1]

        avg = all_sum / len(data)

        ret = set()
        for elem in data:
            del_avg = elem[1] - avg
            ret.add((elem[0], del_avg))
        return ret

    # delta_prev
    elif index == 3:
        temp_S = data[0][0]
        if temp_S[3] == '*':
            return data  # if there is no year, do nothing

        rank_arr = []
        # put all data in array with index as the rank of year
        for elem in data:
            if len(rank_arr) == 0:
                rank_arr.append(elem)
            else:
                inserted = False
                for i in range(len(rank_arr)-1):
                    if elem[0][3] < rank_arr[i+1][0][3]:
                        rank_arr.insert(i, elem)
                        inserted = True
                        break

                if not inserted:
                    rank_arr.append(elem)

        ret = set()
        ret.add((rank_arr[0][0], rank_arr[0][1]))  # the first one assumes to be a change from 0
        for i in range(1, len(rank_arr)):
            del_prev = rank_arr[i][1] - rank_arr[i-1][1]
            ret.add((rank_arr[i][0], del_prev))

        return ret

    # avg
    elif index == 4:

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


def create_sql(S, R):
    suffix = ""
    if R == 2:
        suffix = "_2"
    elif R == 3:
        suffix = "_3"
    elif R == 4:
        suffix = "_4"

    conditions = ""
    cond_arr = []
    cond_arr[0] = 0 if S[0] == '*' else 1
    cond_arr[1] = 0 if S[1] == '*' else 1
    cond_arr[2] = 0 if S[2] == '*' else 1
    cond_arr[3] = 0 if S[3] == '*' else 1
    cond_arr[4] = 0 if S[4] == '*' else 1

    if cond_arr[0] == 1:
        conditions += "a.id = " + S[0]
        if sum(cond_arr[1:]) > 0:
            conditions += ", "

    if cond_arr[1] == 1:
        conditions += "v.id = " + S[1]
        if sum(cond_arr[2:]) > 0:
            conditions += ", "

    if cond_arr[2] == 1:
        conditions += "v.type = " + S[2]
        if sum(cond_arr[2:]) > 0:
            conditions += ", "

    if cond_arr[3] == 1:
        conditions += "v.year = " + S[3]
        if sum(cond_arr[2:]) > 0:
            conditions += ", "

    if cond_arr[1] == 1:
        conditions += "co.coauthors = " + S[4]


    request = "SELECT COUNT(p.id)" \
              "FROM authors" + suffix + "a, " \
                    "venue" + suffix + "v, " \
                    "papers" + suffix + "p, " \
                    "paperauths" + suffix + "pa, " \
                    "co_authors" + suffix + "co" \
              "WHERE a.id = pa.authid, p.id = pa.paperid, v.id = p.venue" + conditions + ";"

    return request


def extract(S, di, doms, ce, tau, R):
    phi = set()
    for v in doms[di]:
        S_prime = deepcopy(S)
        S_prime[di] = v
        M_prime = recur_extract(S_prime, tau, ce)
        phi.add((S_prime, M_prime))

    return phi


def recur_extract(S, level, ce, doms, R):
    if level > 1:
        res_set = set()
        D = ce[level-1][1]
        for v in doms[D]:
            Sv = deepcopy(S)
            Sv[D] = v
            Mv_prime = recur_extract(Sv, level-1, ce, doms)
            res_set.add((Sv, Mv_prime))

        M_prime = extractors(D, res_set)

    else:
        M_prime = set()  # should be the returned value of create_sql(S, R)

    return M_prime
