class DP_FIB_Memo:

    memo = []

    def __init__(self, n):

        self.memo.append(1) #index zero
        self.memo.append(1) #index one

        for x in range(2, n):

            self.memo.append(self.memo[x - 1] + self.memo[x - 2])

        pprint(self.memo)


obj = DP_FIB_Memo(6)
