// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
int countWord = 0;

// Hash table
node *table[N];

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Simple hash function based on the first character
    // Use lowercase to handle case-insensitive dictionary
    return tolower(word[0]) - 'a';
}

// Case-insensitive string comparison function
int stricmp(const char *str1, const char *str2)
{
    while (*str1 && *str2)
    {
        int diff = tolower(*str1) - tolower(*str2);
        if (diff != 0)
            return diff;
        str1++;
        str2++;
    }
    return tolower(*str1) - tolower(*str2);
}

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int hashNum = hash(word);
    // Create cursor variable
    node *cursor = table[hashNum];
    // Loop until the end of the linked list
    while (cursor != NULL)
    {
        // Check if the words are the same (case-insensitive)
        if (stricmp(cursor->word, word) == 0)
        {
            return true;
        }
        // Otherwise, move cursor to the next node
        cursor = cursor->next;
    }
    return false;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *DictFile = fopen(dictionary, "r");

    // Check if return value is NULL
    if (DictFile == NULL)
    {
        return false;
    }

    // Read strings from file one at a time
    char str[LENGTH + 1];
    while (fscanf(DictFile, "%s", str) != EOF)
    {
        // Create a new node for each word
        // Use malloc
        node *temp = malloc(sizeof(node));
        // Check if return value is NULL
        if (temp == NULL)
        {
            return false;
        }
        // Copy word into node using strncpy to prevent buffer overflow
        strncpy(temp->word, str, LENGTH);
        temp->word[LENGTH] = '\0'; // Ensure null-terminated

        // Use the hash function
        int hashNum = hash(str);

        // Point temp to the first node of the linked list
        temp->next = table[hashNum];

        // Point the header to temp
        table[hashNum] = temp;

        countWord += 1;
    }
    // Close the file
    fclose(DictFile);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return countWord;
}

// Recursively free nodes in a linked list
void freenode(node *n)
{
    if (n == NULL)
    {
        return;
    }
    freenode(n->next);
    free(n);
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        freenode(table[i]);
    }
    return true;
}
