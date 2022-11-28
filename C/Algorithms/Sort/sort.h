#ifndef sort_h
#define sort_h

#define LEN 100000
#define TYPE 8

extern int g_master[];
extern int g_array[];
extern int g_buf[];

void swap(int array[], int a, int b);
void shuffle(int seed, int array[]);

// Sort Function
void bubble(void);
void selection(void);
void insert(void);
void comb(void);
void merge(void);
void quick(void);
void radix(void);
void heap(void);

// Sub Function
void func_divide(int l, int r);
void func_merge(int l, int m, int r);
void func_quick(int l, int r);
void func_upheap(int c);
void func_downheap(int n);
int median(int a, int b, int c);

#endif
