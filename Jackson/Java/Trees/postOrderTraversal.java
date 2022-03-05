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
    