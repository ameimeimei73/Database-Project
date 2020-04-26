import pandas as pd
import numpy as np
import heapq
from ScoreFunction import insight_score
from Extractor import extract

authorid = pd.read_csv('authorid.csv', index_col = False, header = None)
authorid = list(np.array(authorid).reshape(-1))

venueid = pd.read_csv('venueid.csv', index_col = False, header = None)
venueid = list(np.array(venueid).reshape(-1))

venuetype = pd.read_csv('venuetype.csv', index_col = False, header = None)
venuetype = list(np.array(venuetype).reshape(-1))

venueyear = pd.read_csv('venueyear.csv', index_col = False, header = None)
venueyear = list(np.array(venueyear).reshape(-1))

coauthors = pd.read_csv('coauthors.csv', index_col = False, header = None)
coauthors = list(np.array(coauthors).reshape(-1))

dimesions = [authorid, venueid, venuetype, venueyear, coauthors]
type = [1, 2]

def EnumerateInsight(s, di, ce, H, R, k, tau):
    if isValid(s, di, ce):
        phi = extract(s, di, dimesions, ce, tau, R)
        for t in type:
            score = insight_score(phi, t, 270687)
            if len(H) < k:
                heapq.heappush(H, (score, [s, di, ce, t]))
            elif len(H) == k:
                uk = H[0]
                ubk = uk[0]
                if score > ubk:
                    heapq.heappush(H, (score, [s, di, ce, t]))
                    heapq.heappop(H)
    for d in dimesions[di]:
        si = s
        si[di] = d
        for j in range(0, len(s)):
            if si[j] == '*':
                EnumerateInsight(si, j, ce, H, R, k, tau)

def isValid(s, di, ce):
    n = len(ce)
    print(n)
    for i in range(1, n):
        if ce[i][1] != di and s[ce[i][1]] == '*':
            return False
    return True








