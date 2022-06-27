#include "lists.h"

/**
 * check_cycle - function checks if a linked list conatins a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	if (!list)
		return (0);

	while (slow && fast && fast -> next)
	{
		slow = slow -> next;
		fast = fast -> next -> next;
		if (fast == slow)
			return (1);
	}
	return (0);
}
