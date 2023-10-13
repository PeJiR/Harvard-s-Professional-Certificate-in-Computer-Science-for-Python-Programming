#include <cs50.h>
#include <stdio.h>

void print_line(int height, int row)
{
    // Print spaces to align the pyramid to the right.
    for (int i = 0; i < height - row - 1; i++)
    {
        printf(" ");
    }

    // Print hashes for the current row of the pyramid.
    for (int i = 0; i < row + 1; i++)
    {
        printf("#");
    }

    // Print spaces between the two pyramids.
    for (int i = 0; i < 2; i++)
    {
        printf(" ");
    }

    // Print hashes for the current row of the second pyramid.
    for (int i = 0; i < row + 1; i++)
    {
        printf("#");
    }

    // Print a newline character.
    printf("\n");
}

void print_pyramid(int height)
{
    for (int row = 0; row < height; row++)
    {
        print_line(height, row);
    }
}

int main()
{
    int height;

    // Prompt the user for the height of the pyramid.
    printf("Height: ");
    scanf("%d", &height);

    // Validate the user's input.
    while (height < 1 || height > 8)
    {
        printf("Invalid height. Please enter a positive integer between 1 and 8: ");
        scanf("%d", &height);
    }

    // Print the pyramid.
    print_pyramid(height);

    return 0;
}
