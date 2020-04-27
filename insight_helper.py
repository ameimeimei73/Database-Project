import pandas as pd
from copy import deepcopy
import numpy as np
import heapq
from ScoreFunction import insight_score
from Extractor import extract

authorid = pd.read_csv('authorid_1.csv', index_col = False, header = None)
authorid = list(np.array(authorid).reshape(-1))

venueyear = pd.read_csv('venueyear_1.csv', index_col = False, header = None)
venueyear = list(np.array(venueyear).reshape(-1))

# coauthors = pd.read_csv('small_coauthors.csv', index_col = False, header = None)
# coauthors = list(np.array(coauthors).reshape(-1))

dimesions = [authorid, venueyear]
type = [1, 2]

def EnumerateInsight(s, di, ce, H, R, k, tau):
    if isValid(s, di, ce, R):
        phi = extract(s, di, dimesions, ce, tau, R)
        for t in type:
            if (t == 2 and s[1] == '*'):
                continue
            score = float(insight_score(phi, t, 5000))
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

    if R == 1 or R == 2:
        for i in range(1, n):
            if ce[i][1] != di and s[ce[i][1]] == '*':
                return False
    elif R == 3:
        for i in range(1, n):
            if ce[i][1] != di and s[ce[i][1]] == '*' and di != 0 and ce[n-1][1] != 0: # s[0] == '*': !(ce[n-1][1] == 0 or di == 0)
                return False
    return True








