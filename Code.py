#include <stdio.h>

int main() {
    int m, n;

    printf("Enter the number of Rows: ");
    scanf("%d", &m);
    
    printf("Enter the number of Columns: ");
    scanf("%d", &n);

    int ar[m][n];

    printf("Enter Elements:\n");
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            scanf("%d", &ar[i][j]);
        }
    }

    printf("The matrix is:\n");
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("\t%d", ar[i][j]);
        }
        printf("\n");
    }

    return 0;
}
