
class Solution {
    public boolean isSymmetric(TreeNode root) {
        TreeNode r1 = root.left;
        TreeNode r2 = root.right;
        return recurse(r1, r2);  
    }
    
    public boolean recurse(TreeNode r1, TreeNode r2){
        if (r1 == null && r2 == null){
            return true;
        }
        if (r1 == null && r2 != null){
            return false;
        }
        if(r1 != null && r2 == null){
            return false;
        }
        if(r1.val != r2.val){
            return false;
        }
        return recurse(r1.left, r2.right) && recurse(r1.right, r2.left);
            
    }
    
}