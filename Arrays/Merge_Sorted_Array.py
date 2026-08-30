class Solution(object):
    def merge(self, nums1, m, nums2, n):
        merged_arr = []
        i = 0
        j = 0
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                merged_arr.append(nums1[i])
                i+=1
            else:
                merged_arr.append(nums2[j])
                j+=1
        while i<m:
            merged_arr.append(nums1[i])
            i+=1
        while j<n:
            merged_arr.append(nums2[j])
            j+=1
        nums1[:]=merged_arr
        