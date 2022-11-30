#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - checks whether list has a cycle or not
 * @list: the list
 * Return: 0 for no cycle and 1 for cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *i, *k;

	if (!list)
		return (0);

	i = list;
	k = list;

	while (i && k && k->next)
	{

		if (k == k->next && k)
			return (1);
		k = k->next;
		i = i->next->next;		
		if (k == i && k && i)
		{
			return (1);
		}
	}
	return (0);
}
