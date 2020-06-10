#include <stdio.h>
#include "DataStructures/list.c"

void print3List(ListNode* headA, ListNode* headB, ListNode* headC) {
    printf("ListA : "); printList(headA);
    printf("ListB : "); printList(headB);
    printf("ListC : "); printList(headC);
    printf("\n");
}

void searchFrom3Lists(ListNode* headA, ListNode* headB, ListNode* headC, int data) {
    if (searchFromList(headA, data) != NULL) printf("[%d] exist in ListA\n", data);
    else printf("[%d] doesn't exist in ListA\n", data);
    
    if (searchFromList(headB, data) != NULL) printf("[%d] exist in ListB\n", data);
    else printf("[%d] doesn't exist in ListB\n", data);
    
    if (searchFromList(headC, data) != NULL) printf("[%d] exist in ListC\n\n", data);
    else printf("[%d] doesn't exist in ListC\n\n", data);
}

void addTo3ListHead(ListNode** headA, ListNode** headB, ListNode** headC, int data) {
    addToListHead(headA, data);
    addToListHead(headB, data);
    addToListHead(headC, data);
    print3List(*headA, *headB, *headC);
}

void addTo3ListTail(ListNode** headA, ListNode** headB, ListNode** headC, int data) {
    addToListTail(headA, data);
    addToListTail(headB, data);
    addToListTail(headC, data);
    print3List(*headA, *headB, *headC);
}

int main(void) {
    ListNode* headA = NULL;
    ListNode* headB = NULL;
    ListNode* headC = NULL;
    print3List(headA, headB, headC);// Print List
    
    makeListNode(&headA, 5, NULL);
    addToListHead(&headB, 5);
    addToListTail(&headC, 5);
    print3List(headA, headB, headC);// Print List
    
    addTo3ListHead(&headA, &headB, &headC, 4);
    addTo3ListTail(&headA, &headB, &headC, 6);
    addTo3ListHead(&headA, &headB, &headC, 3);
    addTo3ListTail(&headA, &headB, &headC, 7);
    addTo3ListHead(&headA, &headB, &headC, 2);
    addTo3ListTail(&headA, &headB, &headC, 8);
    
    for (int i = 0; i <= 10; i++) searchFrom3Lists(headA, headB, headC, i);
    
    printf("[5]'s next is [%d]\n\n", searchFromList(headA, 5)->next->data);
    
    printf("ListA : "); printList(headA);
    deleteFromList(&headA, 2);
    deleteFromList(&headA, 5);
    deleteFromList(&headA, 8);
    deleteFromList(&headA, 0);
    deleteFromList(&headA, 9);
    printf("ListA : "); printList(headA);
    
    return 0;
}
