#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>


int main(void)
{
    //Ask user for the credit card number and store the input in a string
    string card_number;
    card_number = get_string("Number: ");

    // Store the string length
    int string_length = strlen(card_number);

    //Iterate through each character to check if it is a digit
    for (int character = 0; character < string_length; character++)
    {
        if (!isdigit(card_number[character]))
        {
            printf("INVALID\n");
            break;
        }
    }

    //Calculate the check_sum
    int check_sum = 0;

    for (int character = string_length - 1; character >= 0; character -= 2)
    {
        check_sum += card_number[character] - '0';
    }

    for (int character = string_length - 2; character >= 0; character -= 2)
    {
        int digit = ((card_number[character] - '0') * 2);

        while (digit > 0)
        {
            check_sum += (digit % 10);
            digit /= 10;
        }
    }

    //Print the credit card provider
    if (check_sum % 10 == 0 && string_length == 15 && card_number[0] == '3' && card_number[1] == '4')
    {
        printf("AMEX\n");
    }
    else if (check_sum % 10 == 0 && string_length == 15 && card_number[0] == '3' && card_number[1] == '7')
    {
        printf("AMEX\n");
    }
    else if (check_sum % 10 == 0 && string_length == 13 && card_number[0] == '4')
    {
        printf("VISA\n");
    }
    else if (check_sum % 10 == 0 && string_length == 16 && card_number[0] == '4')
    {
        printf("VISA\n");
    }
    else if (check_sum % 10 == 0 && string_length == 16 && card_number[0] == '5' && card_number[1] == '1')
    {
        printf("MASTERCARD\n");
    }
    else if (check_sum % 10 == 0 && string_length == 16 && card_number[0] == '5' && card_number[1] == '2')
    {
        printf("MASTERCARD\n");
    }
    else if (check_sum % 10 == 0 && string_length == 16 && card_number[0] == '5' && card_number[1] == '3')
    {
        printf("MASTERCARD\n");
    }
    else if (check_sum % 10 == 0 && string_length == 16 && card_number[0] == '5' && card_number[1] == '4')
    {
        printf("MASTERCARD\n");
    }
    else if (check_sum % 10 == 0 && string_length == 16 && card_number[0] == '5' && card_number[1] == '5')
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }

}
