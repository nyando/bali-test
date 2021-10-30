public class IntReverse {

    public static int reverse(int reverseMe) {
        int acc = 0;
        while (reverseMe != 0) {
            acc *= 10;
            acc += reverseMe % 10;
            reverseMe /= 10;
        }
        return acc;
    }

    public static void main(String[] args) {
        System.out.println(reverse(123456));
    }

}
