#include <stdio.h>
#include <time.h>
#include "sort.h"

#define LOOP 10

double sort(char sortName[], int type);

int main(void) {
    int i, type;
    double sort_time[TYPE];
    char sort_name[TYPE][10] = {
        "BUBBLE", "SELECTION", "INSERT", "COMB", "MERGE",
        "QUICK", "RADIX", "HEAP",
    };
    
    // Initialization
    for (i = 0; i < LEN; i++)
        g_master[i] = i;
    for (type = 0; type < TYPE; type++)
        sort_time[type] = 0;
    
    // Sort
    for (i = 0; i < LOOP; i++) {
        printf("%3d|", i + 1);
        shuffle(i, g_master);
        for (type = 0; type < TYPE; type++)
            sort_time[type] += sort(sort_name[type], type);
        printf("\n");
    }
    
    // Print Time
    printf("\n---- DATA LEN %7d ----\n", LEN);
    for (type = 0; type < TYPE; type++)
        printf("%-10s-%9.6f [sec]\n", sort_name[type], sort_time[type] / LOOP);
    printf("--------------------------\n");
    return 0;
}

double sort(char sort_name[], int type) {
    int i, e;
    clock_t start, stop;
    
    for (i = 0; i < LEN; i++)
        g_array[i] = g_master[i];
    printf(" %s |", sort_name);
    
    start = clock();
    switch (type) {
        case 0: bubble();    break;
        case 1: selection(); break;
        case 2: insert();    break;
        case 3: comb();      break;
        case 4: merge();     break;
        case 5: quick();     break;
        case 6: radix();     break;
        case 7: heap();      break;
        default: printf("[ERROR: sort/switch %d]\n", type); return 0;
    } stop = clock();
    
    // Check
    for (i = 0, e = 0; i < LEN; i++)
        if (g_array[i] != i)
            e++;
    if (e != 0)
        printf("[ERROR: sort/check %d]\n", e);
    
    return (double) (stop - start) / CLOCKS_PER_SEC;
}
