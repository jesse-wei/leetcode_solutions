
import java.util.ArrayList;
import java.util.List;
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
     List<Integer> sol = new ArrayList<>();

        sol = recurse(root, sol);
        return sol;
            
        
    }
    
    public List<Integer> recurse(TreeNode r, List<Integer> sol){
        
        if (r == null){
            return sol;
        }
        recurse(r.left, sol);
        sol.add(r.val);
        recurse(r.right, sol);
        
        return sol;
        
    }
    
}
    