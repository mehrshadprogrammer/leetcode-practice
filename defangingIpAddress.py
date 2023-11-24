class Solution:
    def debangingIPadd(self, addr: str) -> str:
        newAddr = addr.replace('.', '[.]')
        return newAddr

solution = Solution()
str = solution.debangingIPadd("192.168.11.1")
print(str)