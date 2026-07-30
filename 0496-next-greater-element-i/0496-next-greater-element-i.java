class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] result = new int[nums1.length]; 
        for(int i=0; i<nums1.length; i++){
            //pick a number 
            int a = nums1[i];//[4,1,2]
            //search 'a' in num2
            int index = 0;
            for(int j=0; j<nums2.length; j++){
                if(a==nums2[j])
                {
                index=j;
                break;
                }
            }
            int nge = -1; 
                //now search for next greater element in nums2 
            for(int k=index+1; k<nums2.length; k++){
                if(nums2[k]>a) {
                nge = nums2[k];
                    break;
                }
            }
            result[i]= nge;
        }
        return result;
    }
}
