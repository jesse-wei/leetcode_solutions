class Solution {
    public boolean isPalindrome(int x) {
        String nx = String.valueOf(x);
        int l = 0;
        int r = nx.length() - 1;
        while (l <= r){
            if(nx.charAt(l) != nx.charAt(r)){
                return false;  
            }
            else{
                r--;
                l++;
                
            }
        }
        return true;
        
    }
}