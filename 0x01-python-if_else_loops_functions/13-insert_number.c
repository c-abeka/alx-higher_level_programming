#include "lists.h"

/**
 * insert_node - adds node to sorted singly linked list
 * @head: head of current list
 * @number: the number to add
 * Return: NULL on fail and Address of new node if success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current = NULL, *buffer;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	if (*head)
	{
		current = *head;
		if (number <= current->n)
		{
			new_node->next = current;
			*head = new;
		}
		else
		{
			while (current->next)
			{
				if (number <= current->next->n)
				{
					buffer = current->next;
					current->next = new;
					new->next = buffer;
					return(*head);
				}
				current = current->next;
			}
			buffer = current->next;
			current->next = new;
			new->next = buffer;
		}
		return (*head);
	}
	new->next = NULL;
	*head = new;
	return(*head);
}

