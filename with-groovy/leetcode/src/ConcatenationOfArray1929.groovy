def array = new ArrayList()
array.add(1)
array.add(2)
array.add(1)

int[] nums = new int[3]
nums[0] = 1
nums[1] = 2
nums[2] = 1

println(doubleArrayWithOutList(nums))


def doubleArray(List array){

    List<Integer> result = new ArrayList<>();
    for (Integer element: array )
        result << element
    for( Integer element: array)
        result << element

    return result
}
int[] doubleArrayWithOutList(int[] nums){
    int length = nums.length
    int[] result = new int[length * 2]
    for (int i = 0 ; i < length ; i ++)
        result[i] = nums[i]
    for (int i = 0 ; i < length ; i++)
        result [i + length] = nums[i]

    return result
}