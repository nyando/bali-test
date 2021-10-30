public class PrimeSieve {

    public static void sieve(boolean[] primes, int size) {
        for (int i = 0; i <= size; i++) {
            primes[i] = true;
        }

        for (int p = 2; p * p <= size; p++) {
            if (primes[p]) {
                for (int i = p * p; i <= size; i += p) {
                    primes[i] = false;
                }
            }
        }
    }

    public static void main(String[] args) {
        int max = 2_000_000_000;
        boolean[] primes = new boolean[max + 1];
        sieve(primes, max);

        for (int i = 0; i <= max; i++) {
            if (primes[i]) {
                System.out.println(i);
            }
        }
    }

}