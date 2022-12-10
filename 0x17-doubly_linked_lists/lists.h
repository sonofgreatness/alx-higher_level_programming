#ifndef LISTS_H
#define LISTS_H
#include <stddef.h>

/*
*Data structure to handle
*doubly linked list
**/
typedef struct dlistint_s
{
int n;
struct dlistint_s *prev;
struct dlistint_s *next;
} dlistint_t;
size_t print_dlistint(const dlistint_t *h);
#endif
