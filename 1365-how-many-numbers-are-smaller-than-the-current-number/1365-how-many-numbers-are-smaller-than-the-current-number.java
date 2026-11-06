class Solution {
    public int[] smallerNumbersThanCurrent(int[] nums) {
        int[] arr=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            arr[i]=nums[i];
        }
     Arrays.sort(arr);
     HashMap<Integer,Integer> hm=new HashMap<>();
     for (int i=arr.length-1;i>=0;i--){
        hm.put(arr[i],i);

     }  
     for(int i=0;i<nums.length;i++){
        arr[i]=hm.get(nums[i]);
     } 
     return arr;
    }
}