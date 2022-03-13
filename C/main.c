#include <stdio.h>
#include "DataStructures/list.c"

int main(void) {
    List list = new_List();
    print_List(list);
    
    add_to_List(&list, 1);
    add_to_List(&list, 2);
    add_to_List(&list, 3);
    add_to_List_Tail(&list, 4);
    add_to_List_Tail(&list, 5);
    add_to_List_Tail(&list, 6);
    print_List(list);
    
    delete_from_List(&list, 0);
    print_List(list);
    
    delete_from_List(&list, 6);
    print_List(list);
    
    delete_from_List(&list, 3);
    print_List(list);
    
    delete_from_List(&list, 1);
    print_List(list);
    
    ListNode *node1 = search_List(list, 1);
    ListNode *node2 = search_List(list, 2);
    
    if (node1 == NULL) print("node 1 is null.\n");
    else print("node 1 is %d.\n", node1->data);
    
    if (node2 == NULL) print("node 2 is null.\n");
    else print("node 2 is %d.\n", node2->data);
    
    return 0;
}



void add_to_List(List *list, int data)
void add_to_List_Tail(List *list, int data)
int delete_from_List(List *list, int data)
ListNode *search_List(List list, int data)
void print_List(List list)
