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
	listint_t *current;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while(*head->n <= number)
		{
			if (*head->next == NULL)
				*head->next = new


