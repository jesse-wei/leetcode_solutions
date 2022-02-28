//Returns minimum depth of a binary tree
package Trees;
class Solution {
    public int minDepth(TreeNode root) {
        int sol = 0;
        return recurse(root, sol);
    }
    public int recurse(TreeNode r, int sol){
        if(r == null){
            return sol;
        }
        if(r.right != null && r.left == null){
            return recurse(r.right, sol + 1);
        }
        if(r.left != null && r.right == null){
            return recurse(r.left, sol + 1);
        }
        return Math.min(recurse(r.left, sol + 1), recurse(r.right, sol + 1));

    }
}