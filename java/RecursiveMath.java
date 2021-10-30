public class RecursiveMath {

    public static int increment(int x) {
        return (x & 1) == 0 ? x | 1 : increment(x >> 1) << 1;
    }

    public static int decrement(int x) {
        return (x & 1) == 1 ? x ^ 1 : (decrement(x >> 1) << 1) ^ 1;
    }

    public static int add(int x, int y) {
        return x == 0 ? y : (y == 0 ? x : add(decrement(x), increment(y)));
    }

    public static int multiply(int x, int y) {
        return x == 0 || y == 0 ? 0 : (y == 1 ? x : add(x, multiply(x, decrement(y))));
    }

    public static void main(String[] args) {
        multiply(2, 3);
        multiply(3, 2);
        multiply(0, 3);
        multiply(3, 0);
        multiply(1, 3);
        multiply(3, 1);
    }


}
