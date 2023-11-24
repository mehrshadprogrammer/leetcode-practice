class solution:
    def finalValueAfterOperation(self, operation: list[str]) -> str:
        count = 0
        for op in operation:
            if "+" in op:
                count += 1
            else:
                count -=1
        return count