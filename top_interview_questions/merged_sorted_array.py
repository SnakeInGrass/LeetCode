class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Combine two sorted arrays inplace (the first array has empty space at the end).
        """
        if n == 0:
            return

        if m == 0:
            for i, v in enumerate(nums2):
                nums1[i] = v

        nums1_ptr = m-1
        nums2_ptr = n-1
        storage_ptr = m+n-1
        while nums1_ptr >= 0 and nums2_ptr >= 0:
            if nums2[nums2_ptr] > nums1[nums1_ptr]:
                nums1[storage_ptr] = nums2[nums2_ptr]
                nums2_ptr -= 1
            else:
                nums1[storage_ptr] = nums1[nums1_ptr]
                nums1_ptr -= 1
            storage_ptr -= 1
        
        if nums2_ptr < 0:
            return

        if nums1_ptr < 0:
            for i in range(nums2_ptr+1):
                nums1[i] = nums2[i]

list1 = [1,2,3,0,0,0]
Solution().merge(list1, 3, [1,2,4], 3)
print(list1)