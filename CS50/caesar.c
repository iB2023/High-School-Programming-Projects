#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    //condition
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        int key = atoi(argv[1]);
        string plaintext = get_string("plaintext: ");
        //Ciphertext will be followed by the new characters
        printf("ciphertext: ");
    
        for (int i = 0; i < strlen(plaintext); i++)
        {
            if (plaintext[i] >= 97 && plaintext[i] <= 122)
            {
                //ASCII values utilized for calculating key
                printf("%c", (((plaintext[i] - 97) + key) % 26) + 97);
            }
            else if (plaintext[i] >= 65 && plaintext[i] <= 90)
            {
                //ASCII values utilized for calculating key
                printf("%c", (((plaintext[i] - 65) + key) % 26) + 65);
            }
            else
            {
                //What happens if the character is not a letter
                printf("%c", plaintext[i]);
            }
        }
        //New line
        printf("\n");
    }
}
