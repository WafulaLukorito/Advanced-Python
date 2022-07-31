from collections import Counter
from typing import List


class Solution:
    def mostFrequent( nums: List[int], key: int) -> int:
        key1 = nums.index(key)
        list1 = nums[key1+1:]
        myCounter = Counter(list1)
        numOcc = (myCounter.values())
        list2 = []
        for num in numOcc:
            list2.append(num)
        print (list2)
        list2.sort()
        print (list2)
        maxOcc = list2[0]
        print (myCounter)
        for k, v in myCounter.items():
            if v == maxOcc:
                return k

    nums = [2,2,2,2,3]
    key = 2

    print(mostFrequent(nums, key))