package LinkedList;

// Use two pointers, one moving one step and another going 2. At some point, they will intersect (Floyd's Cycle Finding Algorithm)
public class findCycle {
    public boolean hasCycle(ListNode head) {
        if (head == null){
            return false;
        }
        if (head.next == null){
            return false;
        }
        ListNode s = head;
        ListNode f = head.next;
        return recurse(s, f);
    }
    public boolean recurse(ListNode s, ListNode f){
        if (s.next == null || s == null){
            return false;
        }
        if (f.next == null || f.next.next == null){
            return false;
        }
        if (s == f){
            return true;
        }
        return recurse(s.next, f.next.next);
        
    }
}