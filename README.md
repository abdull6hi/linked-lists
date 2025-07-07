# Linked List Implementation in Python
## Features

* **Insert at End**: Adds a new node at the end of the list.
* **Insert at Beginning**: Adds a new node at the beginning of the list.
* **Delete Node**: Removes a node with a specified key from the list.
* **Search**: Searches for a node with a specific key in the list.
* **Reverse**: Reverses the entire list.
* **Display**: Prints the contents of the list in a readable format.


### `Node` Class

This class represents a single node in the linked list. Each node contains:

* `data`: The data stored in the node.
* `next`: A pointer to the next node in the list (initially set to `None`).

### `LinkedList` Class

This class represents the linked list and contains the following methods:

* **`__init__()`**: Initializes an empty linked list.
* **`insert_at_end(data)`**: Inserts a new node with the given `data` at the end of the list.
* **`insert_at_beginning(data)`**: Inserts a new node with the given `data` at the beginning of the list.
* **`delete_node(key)`**: Deletes the first occurrence of the node with the given `key`.
* **`search(key)`**: Searches for the node with the given `key` in the list and prints if found.
* **`reverse()`**: Reverses the linked list.
* **`display()`**: Prints the linked list in a readable format, e.g., `10 → 20 → 30 → None`.

## Usage

1. **Create a LinkedList:**

```python
ll = LinkedList()
```

2. **Insert elements at the end:**

```python
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
```

3. **Insert element at the beginning:**

```python
ll.insert_at_beginning(5)
```

4. **Display the list:**

```python
ll.display()  # Output: 5 → 10 → 20 → 30 → None
```

5. **Search for an element:**

```python
ll.search(20)  # Output: 20 found in list.
```

6. **Delete a node by value:**

```python
ll.delete_node(10)
ll.display()  # Output: 5 → 20 → 30 → None
```

7. **Reverse the list:**

```python
ll.reverse()
ll.display()  # Output: 30 → 20 → 5 → None
```






