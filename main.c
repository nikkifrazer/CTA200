#include <stdio.h>
#include "average.h"


int main() {
    double arr[] = {1.5, 2.0, 3.0, 4.0};

    double result = average(4, arr);

    printf("The average of 1.5, 2, 3 and 4 is: %.4f\n", result);
    return 0;    
}

/* Changed 1 to 1.5, and averaged the four numbers */

