#include <iostream>
#include <string>


using namespace std;

pair<long, long> pars[100000];
long n;

void siftDown(long i) {
    long left = 2 * i + 1;
    long right = 2 * i + 2;
    long j;
    if (right < n && pars[right].first < pars[i].first) {
        j = right;

    } else {
        j = i;
    }

    if (left < n && pars[left].first < pars[j].first) {
        j = left;
    }
    if (i != j) {
        swap(pars[i], pars[j]);
        siftDown(j);
    }
}

void siftUp(long i) {
    if (i != 0) {
        if (pars[(i - 1) / 2].first > pars[i].first) {
            swap(pars[(i - 1) / 2], pars[i]);
            siftUp((i - 1) / 2);
        }
    }
}


long extractMin() {
    long ans = pars[0].first;
    swap(pars[0], pars[n - 1]);
    n--;
    siftDown(0);
    return ans;
}

void decreaseKey(long x, long y) {
    long i;
    for (i = 0; i < n; i++) {
        if (pars[i].second == x) {
            break;
        }
    }
    pars[i].first = y;
    siftUp(i);
}

void push(long obj, long i) {
    n++;
    pars[n - 1].first = obj;
    pars[n - 1].second = i;
    siftUp(n - 1);
}

int main() {
    string required;
    freopen("priorityqueue.in", "r", stdin);
    freopen("priorityqueue.out", "w", stdout);
    long i = 1;
    n = 0;
    while (cin >> required) {
        if (required == "push") {
            int value;
            cin >> value;
            push(value, i);
        }
        if (required == "extract-min") {
            if (n == 0) {
                cout << "*\n";
            } else {
                cout << extractMin() << endl;
            }
        }
        if (required == "decrease-key") {
            long x, y;
            cin >> x >> y;
            decreaseKey(x, y);
        }
        i++;
    }
}