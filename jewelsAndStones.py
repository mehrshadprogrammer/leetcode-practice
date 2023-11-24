class Solution:
    def numJewelsInStone(jewels:str, stones:str):
        check_jewels = set(jewels)
        count = 0
        for ch in stones:
            if ch in check_jewels:
                count += 1
        return count
    count = numJewelsInStone(jewels="z", stones="ZZ")
    print(count)