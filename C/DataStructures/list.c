#ifndef INCLUDED_STDLIB_H_
#define INCLUDED_STDLIB_H_
#include <stdlib.h>
#endif

typedef struct listNode {
    int data;
    struct listNode *next;
} ListNode;

void makeListNode(ListNode** node, int data, ListNode* next);
void addToListHead(ListNode** node, int data);
void addToListTail(ListNode** node, int data);
void deleteFromList(ListNode** node, int data);
ListNode *searchFromList(ListNode* node, int data);
void printList(ListNode* node);


void makeListNode(ListNode** node, int data, ListNode* next) {
    ListNode* buf = (ListNode*) malloc(sizeof(ListNode));
    buf->data = data;
    buf->next = next;
    *node = buf;
}


void addToListHead(ListNode** node, int data) {
    makeListNode(node, data, *node);
}


void addToListTail(ListNode** node, int data) {
    if (*node == NULL) {
        makeListNode(node, data, NULL);
    } else if ((*node)->next == NULL) {
        makeListNode(&(*node)->next, data, NULL);
    } else {
        addToListTail(&(*node)->next, data);
    }
}


void deleteFromList(ListNode** node, int data) {
    if ((*node)->data == data) {
        free(*node);
        *node = (*node)->next;
    } else if ((*node)->next == NULL) {
        return;
    }else if ((*node)->next->data == data) {
        free((*node)->next);
        (*node)->next = (*node)->next->next;
    } else {
        deleteFromList(&(*node)->next, data);
    }
}


ListNode *searchFromList(ListNode* node, int data) {
    return (node == NULL || node->data == data) ? node : searchFromList(node->next, data);
}


void printList(ListNode* node) {
    if (node == NULL) {
        printf("[NULL]\n");
    } else {
        printf("[%d", node->data);
        
        while ((node = node->next) != NULL) printf(", %d", node->data);
        
        printf("]\n");
    }
}
