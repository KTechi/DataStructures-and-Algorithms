#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode {
    struct ListNode *next;
    int data;
} ListNode;
typedef struct List {
    struct ListNode *head;
} List;

ListNode *new_ListNode(int data) {
    ListNode *buf = (ListNode*) malloc(sizeof(ListNode));
    buf->next = NULL;
    buf->data = data;
    return buf;
}
List new_List() {
    List *buf = (List*) malloc(sizeof(List));
    buf->head = NULL;
    return *buf;
}

void add_to_List(List *list, int data) {
    ListNode *node = new_ListNode(data);
    node->next = list->head;
    list->head = node;
}
void add_to_List_Tail(List *list, int data) {
    ListNode *node = new_ListNode(data);
    if (list->head == NULL) {
        list->head = node;
        return;
    }
    ListNode *tail = list->head;
    for (; tail->next != NULL; tail = tail->next);
    tail->next = node;
}
int delete_from_List(List *list, int data) {
    if (list->head == NULL) return -1;
    if (list->head->data == data) {
        ListNode *del = list->head;
        list->head = del->next;
        free(del);
        return 1;
    }
    for (ListNode *node = list->head; node->next != NULL; node = node->next) {
        if (node->next->data == data) {
            ListNode *del = node->next;
            node->next = del->next;
            free(del);
            return 1;
        }
    }
    return -1;
}
ListNode *search_List(List list, int data) {
    for (ListNode *node = list.head;; node = node->next)
        if (node == NULL || node->data == data)
            return node;
}

void print_List(List list) {
    if (list.head == NULL) {
        printf("[NULL]\n");
    } else {
        ListNode *node = list.head;
        printf("[%d", node->data);
        while ((node = node->next) != NULL) printf(", %d", node->data);
        printf("]\n");
    }
}
