class Solution(object):
    def removeElement(self, num, val):
        i = 0
        for j in range(len(num)):
            if num[j] != val:
                num[i] = num[j]
                i += 1

        return i
        