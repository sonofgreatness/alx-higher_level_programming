#include "lists.h"
/*
*Function that prints all the elements
*of a dlistint_t list.
*/
size_t
/*DEFINITION*/
print_dlistint(const dlistint_t *h)
{
size_t sum_of_nodes = 0;
if (h != NULL)
sum_of_nodes++;

while (h->next != NULL)
{
sum_of_nodes++;
h = h->next;
}

return (sum_of_nodes);
}
