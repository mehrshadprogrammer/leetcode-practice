
int[] nums = [1,1,1,1]
println(numIdenticalPairs(nums))


int numIdenticalPairs(int[] nums){
    def result = 0
    Map<Integer, Integer> countMap = new HashMap<>()
    for (int item : nums){
        result += countMap.getOrDefault(item, 0)
        countMap.put(item, countMap.getOrDefault(item, 0) + 1)
    }
    return result
}

