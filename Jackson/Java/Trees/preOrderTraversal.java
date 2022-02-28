package Trees;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        
            List<Integer> sol = new ArrayList<Integer>();

        sol = recurse(root, sol);
        return sol;
            
        
    }
    
    public List<Integer> recurse(TreeNode r, List<Integer> sol){
        
        if (r == null){
            return sol;
        }
       
        sol.add(r.val);
        recurse(r.left, sol);
        recurse(r.right, sol);
        
      
        
        return sol;
        
    }
    
}