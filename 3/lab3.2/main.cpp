#include "fstream"

using namespace std;


void siftDown(int *array, int root, int bottom) {
    int maxChild;     // макс потомок
    int done = 0;
    while ((root * 2 <= bottom) && (!done)) {
        if (root * 2 == bottom)    // если мы в последнем ряду, запоминаем левый
            maxChild = root * 2;
        else if (array[root * 2] > array[root * 2 + 1])
            maxChild = root * 2;
        else                         // иначе запоминаем больший потомок из двух
            maxChild = root * 2 + 1;

        if (array[root] < array[maxChild]) {                // если элемент вершины меньше максимального
            swap(array[root], array[maxChild]);
            root = maxChild;
        } else
            done = 1;
    }
}

void heapSort(int *numbers, int array_size) {
    for (int i = (array_size / 2) - 1; i >= 0; i--)
        siftDown(numbers, i, array_size - 1);        // нижний ряд
    for (int i = array_size - 1; i >= 1; i--) {
        swap(numbers[0], numbers[i]);         // просеиваются остальные
        siftDown(numbers, 0, i - 1);
    }
}

int main() {
    int n;
    ifstream cin("sort.in");
    ofstream cout("sort.out");
    cin >> n;
    int a[n];
    for (auto &x : a) cin >> x;

    heapSort(a, n);

    for (int i = 0; i < n; i++)
        cout << a[i] << ' ';
    return 0;
}