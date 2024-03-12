public class Main {
    public static void main(String[] args) {
        Functions functions = new Functions();
        
        // System.out.println(functions.isPalindrome(args[0]));
        
        int[] array = new int[]{1, 3, 5, 8, 13, 17, 34, 37};
        int target1 = 21;
        int target2 = 23;
        
        System.out.println(functions.isSumExists(array, target2));

    }
    
}
