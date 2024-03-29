#include <cs50.h>
#include <stdio.h>

int main(void)
{ // Declare the necessary variables.
    int start_population;
    int end_population;
    int years_passed = 0;

    // Prompt the user for the start and end population sizes.
    printf("Start size: ");
    scanf("%d", &start_population);
    while (start_population < 9)
    {
        printf("Start size must be at least 9.\n");
        printf("Start size: ");
        scanf("%d", &start_population);
    }

    printf("End size: ");
    scanf("%d", &end_population);
    while (end_population < start_population)
    {
        printf("End size must be at least the start size.\n");
        printf("End size: ");
        scanf("%d", &end_population);
    }

    // Calculate the number of years required for the population to reach the end size.
    // If the start and end population sizes are the same, print "Years: 0" and exit.
    if (start_population == end_population)
    {
        printf("Years: 0\n");
        return 0;
    }

    do
    {
        start_population = start_population + (start_population / 3) - (start_population / 4);
        years_passed++;
    }
    while (start_population < end_population);

    // Print the number of years required for the llama population to reach the end size.
    printf("Years: %d\n", years_passed);

    return 0;
}