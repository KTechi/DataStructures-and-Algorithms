#include <stdlib.h>
#include "sort.h"

int g_master[LEN];
int g_array[LEN];
int g_buf[LEN];

void swap(int array[], int a, int b) {
    int tmp = array[a];
    array[a] = array[b];
    array[b] = tmp;
}

void shuffle(int seed, int array[]) {
    srand(seed);
    for (int a = 0; a < LEN; a++)
        swap(array, a, rand() % LEN);
}

void bubble(void) {
    for (int a = 0; a < LEN - 1; a++)
    for (int b = 0; b < LEN-a-1; b++)
        if (g_array[b+1] < g_array[b])
            swap(g_array, b, b+1);
}

void selection(void) {
    int a, b, min;
    for (a = 0; a < LEN - 1; a++) {
        for (b = a + 1, min = a; b < LEN; b++)
            if (g_array[b] < g_array[min])
                min = b;
        swap(g_array, a, min);
    }
}

void insert(void) {
    for (int a = 1; a < LEN; a++)
    for (int b = a; 1 <= b && g_array[b] < g_array[b-1]; b--)
        swap(g_array, b, b-1);
}

void comb(void) {
    int gap = LEN, done = 0;
    while (1 < gap || done == 0) {
        gap /= 1.3;
        if (gap == 0) gap = 1;
        else if (gap == 9 || gap == 10) gap = 11;
        done = 1;
        for (int i = 0; i < LEN - gap; i++)
            if (g_array[i+gap] < g_array[i]) {
                swap(g_array, i, i+gap);
                done = 0;
            }
    }
}

void merge(void) {
    func_divide(0, LEN - 1);
}
void func_divide(int l, int r) {
    int m = (l + r) / 2;
    if (r <= l) return;
    func_divide(l, m);
    func_divide(m + 1, r);
    func_merge(l, m + 1, r);
}
void func_merge(int l, int m, int r_) {
    int i = l, left = l, m_ = m - 1;
    while (l <= m_ && m <= r_) g_buf[i++] = g_array[g_array[l] <= g_array[m] ? l++ : m++];
    while (l <= m_) g_buf[i++] = g_array[l++];
    while (m <= r_) g_buf[i++] = g_array[m++];
    for (i = left; i <= r_; i++) g_array[i] = g_buf[i];
}

void quick(void) {
    func_quick(0, LEN - 1);
}
void func_quick(int l, int r) {
    int i = l, j = r, pivot = median(g_array[l], g_array[(l+r)/2], g_array[r]);
    if (r <= l || r == -1) return;
    while (1) {
        while (g_array[i] < pivot && ++i < r);
        while (pivot < g_array[j] && --j < l);
        if (j <= i) break;
        swap(g_array, i, j);
    }
    func_quick(l, i - 1);
    func_quick(j + 1, r);
}
int median(int a, int b, int c) {
    if (a < b) {
        if (b < c) return b;
        else if (c < a) return a;
        return c;
    } else {
        if (c < b) return b;
        else if (a < c) return a;
        return c;
    }
}

#define RADIX 16
void radix(void) {
    int max = LEN, maxDigit;
    int mod = RADIX, div = 1;
    int buckets[RADIX][LEN], bucket_top[RADIX];
    
    for (maxDigit = 0; 0 < max; maxDigit++)
        max /= RADIX;
    for (int i = 0; i < RADIX; i++)
        bucket_top[i] = 0;
    for (int d = 0; d < maxDigit; d++) {
        for (int i = 0; i < LEN; i++) {
            int digit = g_array[i] % mod / div;
            buckets[digit][bucket_top[digit]++] = g_array[i];
        }
        int i = 0;
        for (int j = 0; j < RADIX; j++) {
            for (int k = 0; k < bucket_top[j]; k++)
                g_array[i++] = buckets[j][k];
            bucket_top[j] = 0;
        }
        mod *= RADIX;
        div *= RADIX;
    }
}

#define L_CHILD(i) (((i) + 1) * 2 - 1)
#define R_CHILD(i) (((i) + 1) * 2)
#define PARENT(i)  (((i) + 1) / 2 - 1)
void heap(void) {
    int i = 1;
    while (i < LEN)
        func_upheap(i++);
    while (0 < --i) {
        swap(g_array, 0, i);
        func_downheap(i);
    }
}
void func_upheap(int c) {
    while (0 < c) {
        int p = PARENT(c);
        if (g_array[c] <= g_array[p]) return;
        swap(g_array, p, c);
        c = p;
    }
}
void func_downheap(int n) {
    int p = 0, tmp = 0;
    while (1) {
        int l = L_CHILD(p);
        int r = R_CHILD(p);
        if (n <= l) return;
        if (g_array[tmp] < g_array[l])
            tmp = l;
        if (r < n && g_array[tmp] < g_array[r])
            tmp = r;
        if (tmp == p) return;
        swap(g_array, tmp, p);
        p = tmp;
    }
}
