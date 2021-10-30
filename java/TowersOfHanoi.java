public class TowersOfHanoi {

    static void towerOfHanoi(int n, char from, char to, char aux) {
        if (n == 1) {
            return;
        }
        towerOfHanoi(n - 1, from, aux, to);
        towerOfHanoi(n - 1, aux, to, from);
    }
    
    public static void main(String[] args) {
        int n = 30;
        towerOfHanoi(n, 'A', 'C', 'B');
    }

}