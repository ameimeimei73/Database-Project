from copy import deepcopy
import psycopg2
from psycopg2 import Error

def extractors(index, res_set, S):

    # get the last row of data
    data = {}
    for e in res_set:
        cur_val = res_set[e]
        data[e] = cur_val[-1]


    # rank
    if index == 0:

        temp = sorted(data.items(), key=lambda x: x[1], reverse=True)
        for i in range(len(temp)):
            if temp[i][0] == S:
                return i+1  # rank starts from 1

        # rank_arr = []
        # # put all data in array with index as the rank
        # for key in data:
        #     if len(rank_arr) == 0:
        #         rank_arr.append((key, data[key]))
        #     else:
        #         inserted = False
        #         for i in range(len(rank_arr)):
        #             if data[key] > rank_arr[i][1]:
        #                 rank_arr.insert(i, (key, data[key]))
        #                 inserted = True
        #                 break
        #
        #         if not inserted:
        #             rank_arr.append((key, data[key]))
        #
        # ret = 0
        # for i in range(len(rank_arr)):
        #     if rank_arr[i][0] == S:
        #         ret = i
        #         break
        #
        # return ret

    # percent
    elif index == 1:
        denom = 0
        for key in data:
            denom += data[key]

        ret = round(data[S] / denom * 100, 2)

        return ret

    # delta_avg
    elif index == 2:
        all_sum = 0
        for key in data:
            all_sum += data[key]

        avg = all_sum / len(data)

        ret = data[S] - avg

        return ret

    # delta_prev
    elif index == 3:

        temp = sorted(data.items(), key=lambda x: x[1][3])  # sort by year


        for i in range(len(temp)):
            if temp[i][0] == S:
                if i == 0:
                    return temp[0][1]
                else:
                    return temp[i][1] - temp[i-1][1]

        # rank_arr = []
        # # put all data in array with index as the rank of year
        # for key in data:
        #     if len(rank_arr) == 0:
        #         rank_arr.append((key, data[key]))
        #     else:
        #         inserted = False
        #         for i in range(len(rank_arr)-1):
        #             if key[3] < rank_arr[i+1][0][3]:
        #                 rank_arr.insert(i, (key, data[key]))
        #                 inserted = True
        #                 break
        #
        #         if not inserted:
        #             rank_arr.append((key, data[key]))
        #
        # ret = 0
        # for i in range(len(rank_arr)):
        #     if rank_arr[i][0] == S and i > 0:
        #         ret = rank_arr[i][1] - rank_arr[i-1][1]
        #         break
        #     elif rank_arr[i][0] == S and i == 0:  # the first one assumes to be changed from 0
        #         ret = rank_arr[i][1]
        #
        # return ret


def create_sql(S, R):

    conditions = ""
    cond_arr = [None] * 5
    cond_arr[0] = 0 if S[0] == '*' else 1
    cond_arr[1] = 0 if S[1] == '*' else 1
    cond_arr[2] = 0 if S[2] == '*' else 1
    cond_arr[3] = 0 if S[3] == '*' else 1
    cond_arr[4] = 0 if S[4] == '*' else 1

    if sum(cond_arr) > 0:
        conditions += "WHERE "

    if cond_arr[0] == 1:
        conditions += "aid = " + str(S[0])
        if sum(cond_arr[1:]) > 0:
            conditions += " and "

    if cond_arr[1] == 1:
        conditions += "vid = " + str(S[1])
        if sum(cond_arr[2:]) > 0:
            conditions += " and "

    if cond_arr[2] == 1:
        conditions += "type = " + str(S[2])
        if sum(cond_arr[3:]) > 0:
            conditions += " and "

    if cond_arr[3] == 1:
        conditions += "year = " + str(S[3])
        if sum(cond_arr[4:]) > 0:
            conditions += " and "

    if cond_arr[4] == 1:
        conditions += "coauthors = " + str(S[4])


    request = "SELECT COUNT(*) " \
              "FROM dataset" + str(R) + " " \
              "" + conditions + ";"

    return request


def extract(S, di, doms, ce, tau, R):
    phi = {}
    for v in doms[di]:
        S_prime = deepcopy(S)
        S_prime[di] = v
        M_prime = recur_extract(S_prime, tau, ce, doms, R)
        phi[tuple(S_prime)] = M_prime
    print("return result : ", phi)
    return phi


def recur_extract(S, level, ce, doms, R):
    if level > 1:
        res_set = {}
        D = ce[level-1][1]  # level starts with 1 but array index starts 0
        index = ce[level-1][0]
        for v in doms[D]:
            Sv = deepcopy(S)
            Sv[D] = v
            Mv_prime = recur_extract(Sv, level-1, ce, doms)
            res_set[tuple(Sv)] = Mv_prime

        M_prime = res_set[tuple(S)]

        # only when D == 3 (year), delta_prev (index == 3) is applicable
        if (index == 3 and D == 3) or (index != 3):
            extracted_result = extractors(index, res_set, tuple(S))
            M_prime.append(extracted_result)

        # if want to calculate delta_prev but dimension is not year i.e. all years are the same
        # M_prime will not have new values

    else:
        M_prime = [count_paper(S, R)]  # should be the returned value of create_sql(S, R)

    return M_prime


def count_paper(S, R):
    connection = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="localhost",
                                  port="5432",
                                  database="cs645")

    cursor = connection.cursor()

    sql = create_sql(S, R)
    cursor.execute(sql)
    record = cursor.fetchone()
    res = record[0]

    if (connection):
        cursor.close()
        connection.close()
    return res


