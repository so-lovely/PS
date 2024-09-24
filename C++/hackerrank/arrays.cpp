#include <cstdio>

using namespace std;

int main() {
    unsigned int n;
    scanf("%u", &n);  // Read the number of integers

    int arr[n];  // Create an array of size n

    // Read the integers into the array
    for (unsigned int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);  // Read each integer
    }

    // Print the integers in reverse order
    for (int i = n - 1; i >= 0; i--) {
        printf("%d", arr[i]);  // Use %d to print integers
        if (i != 0) {  // Print space only if it's not the last element
            printf(" ");
        }
    }

    printf("\n");  // Print a newline at the end

    return 0;
}
