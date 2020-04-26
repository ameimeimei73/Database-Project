from Insight import insights
import sys

if __name__ == "__main__":
    R = int(sys.argv[1])
    tau = int(sys.argv[2])
    k = int(sys.argv[3])
    H = insights(R, tau, k)
    print(H)
