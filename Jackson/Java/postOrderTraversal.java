/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
import java.util.ArrayList;
import java.util.List;
class Main{


    
    public List<Integer> postorderTraversal(TreeNode root) {
        
        List<Integer> sol = new ArrayList<>();

        sol = recurse(root, sol);
        return sol;
            
        
    }
    
    public List<Integer> recurse(TreeNode r, List<Integer> sol){
        
        if (r == null){
            return sol;
        }
        recurse(r.left, sol);
        recurse(r.right, sol);
        System.out.println(sol);
        sol.add(r.val);
        
        return sol;
        
    }
    
}
    