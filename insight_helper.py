import pandas as pd
from copy import deepcopy
import numpy as np
import heapq
from ScoreFunction import insight_score
from Extractor import extract

# Import the domain of every dimension
# Question 1
venueid = pd.read_csv('venueid_1.csv', index_col = False, header = None)
venueid = list(np.array(venueid).reshape(-1))
venueyear = pd.read_csv('venueyear_1.csv', index_col = False, header = None)
venueyear = list(np.array(venueyear).reshape(-1))
dimesions = [venueid, venueyear]
#please use sql query "select count(*) from dataset1;" to get the total_tuples
total_tuples = 819

# Question 2
# authorid = pd.read_csv('authorid_2.csv', index_col = False, header = None)
# authorid  = list(np.array(authorid ).reshape(-1))
# venueyear = pd.read_csv('venueyear_2.csv', index_col = False, header = None)
# venueyear = list(np.array(venueyear).reshape(-1))
# dimesions = [authorid, venueyear]
#please use sql query "select count(*) from dataset2;" to get the total_tuples
# total_tuples = 4458

# Question 3
# authorid = pd.read_csv('authorid_3.csv', index_col = False, header = None)
# authorid  = list(np.array(authorid ).reshape(-1))
# venueyear = pd.read_csv('venueyear_3.csv', index_col = False, header = None)
# venueyear = list(np.array(venueyear).reshape(-1))
# dimesions = [authorid, venueyear]
#please use sql query "select count(*) from dataset3;" to get the total_tuples
# total_tuples = 482

# Question 4
# papername = ['systems', 'networks', 'data', 'algorithm', 'distributed', 'neural', 'learning', 'wireless', 'mobile', 'web']
# venueyear = pd.read_csv('venueyear_4.csv', index_col = False, header = None)
# venueyear = list(np.array(venueyear).reshape(-1))
# dimesions = [papername, venueyear]
#please use sql query "select count(*) from dataset4;" to get the total_tuples
# total_tuples = 683752

# Question 5
# papername = ['systems', 'networks', 'data', 'algorithm', 'distributed', 'neural', 'learning', 'wireless', 'mobile', 'web']
# venueyear = pd.read_csv('venueyear_5.csv', index_col = False, header = None)
# venueyear = list(np.array(venueyear).reshape(-1))
# dimesions = [papername, venueyear]
#please use sql query "select count(*) from dataset5;" to get the total_tuples
# total_tuples = 683752

def EnumerateInsight(s, di, ce, H, R, k, tau):
    if isValid(s, di, ce, R):
        phi = extract(s, di, dimesions, ce, tau, R)
        if R == 4:
            type = [1]
        elif R == 5:
            type = [2]
        else:
            type = [1, 2]
        for t in type:
            if (t == 2 and di != 1):
                continue
            score = float(insight_score(phi, t, total_tuples))
            if (score != np.nan):
                if len(H) < k:
                    H.append((score, [s, di, ce, t]))
                    # heapq.heappush(H, (score, [s, di, ce, t]))
                elif len(H) == k:
                    uk = 10
                    ind = -1
                    for i in range(len(H)):
                        if H[i][0] < uk:
                            uk = H[i][0]
                            ind = i
                    if score > uk:
                        del H[ind]
                        H.append((score, [s, di, ce, t]))
                    #uk = H[0]
                    #ubk = uk[0]
                    #if score > ubk:
                        #heapq.heappush(H, (score, [s, di, ce, t]))
                        #heapq.heappop(H)
    for d in dimesions[di]:
        si = deepcopy(s)
        si[di] = d
        for j in range(0, len(s)):
            if si[j] == '*':
                EnumerateInsight(si, j, ce, H, R, k, tau)

def isValid(s, di, ce, R):
    n = len(ce)
    if R == 1 or R == 2 or R == 4 or R == 5:
        for i in range(1, n):
            if ce[i][1] != di and s[ce[i][1]] == '*':
                return False
    elif R == 3:
        for i in range(1, n):
            if ce[i][1] != di and s[ce[i][1]] == '*':
                return False
            if di != 0 and s[0] == '*':
                return False
    return True








