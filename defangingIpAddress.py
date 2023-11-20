# ip = '1.1.1.1'
# newIp = ip.replace('.', '[.]')
# print(newIp)
# class Solution:
#     def debangingIPadd(addr: str) -> str:
#         newAddr = addr.replace('.', '[.]')
#         return newAddr
# str =debangingIPadd("192.168.11.1")
# print(str)

class Solution:
    def debangingIPadd(self, addr: str) -> str:
        newAddr = addr.replace('.', '[.]')
        return newAddr

solution = Solution()
str = solution.debangingIPadd("192.168.11.1")
print(str)