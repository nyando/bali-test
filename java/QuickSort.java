public class QuickSort {

    public static int partition(int[] array, int lo, int hi) {
        int pivot = array[hi];
        int i = lo - 1;

        for (int j = lo; j < hi; j++) {
            if (array[j] <= pivot) {
                i++;
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }

        int temp = array[i + 1];
        array[i + 1] = array[hi];
        array[hi] = temp;

        return i + 1;
    }

    public static void quickSort(int[] array, int lo, int hi) {
        if (lo < hi) {
            int pivot = partition(array, lo, hi);
            quickSort(array, lo, pivot - 1);
            quickSort(array, pivot + 1, hi);
        }
    }

    public static void main(String[] args) {
        int[] sortMe = new int[]{9, 4, 3, 2, 7, 6, 1, 8};
        quickSort(sortMe, 0, 7);
    }

}