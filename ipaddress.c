#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    char ip_address[20];
    printf("Enter the IP address: ");
    scanf("%s", ip_address);

    char *octet;
    octet = strtok(ip_address, ".");
    int octets[4];
    int i = 0;
    while (octet != NULL)
    {
        octets[i++] = atoi(octet);
        octet = strtok(NULL, ".");
    }

    if (octets[0] >= 1 && octets[0] <= 126)
    {
        printf("Class A IP address\n");
    }
    else if (octets[0] >= 128 && octets[0] <= 191)
    {
        printf("Class B IP address\n");
    }
    else if (octets[0] >= 192 && octets[0] <= 223)
    {
        printf("Class C IP address\n");
    }
    else if (octets[0] >= 224 && octets[0] <= 239)
    {
        printf("Class D IP address\n");
    }
    else if (octets[0] >= 240 && octets[0] <= 255)
    {
        printf("Class E IP address\n");
    }
    else
    {
        printf("Invalid IP address\n");
        return 0;
    }

    if (octets[0] == 10)
    {
        printf("Private IP address\n");
    }
    else if (octets[0] == 172 && octets[1] >= 16 && octets[1] <= 31)
    {
        printf("Private IP address\n");
    }
    else if (octets[0] == 192 && octets[1] == 168)
    {
        printf("Private IP address\n");
    }
    else
    {
        printf("Public IP address\n");
    }

    return 0;
}
