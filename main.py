from Insight import insights
import sys

if __name__ == "__main__":
    R = sys.argv[1]
    tau = sys.argv[2]
    k = sys.argv[3]
    H = insights(R, tau, k)
    print(H)
