#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // Get a message from the user
    string message = get_string("Message: ");

    // Iterate over each character in the message
    for (int i = 0, n = strlen(message); i < n; i++)
    {
        char character = message[i];

        // Convert the character to an 8-bit binary representation
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            int bit = (character >> j) & 1;
            print_bulb(bit);
        }

        // Print a newline after each "byte" of 8 symbols
        printf("\n");
    }

    return 0;
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
