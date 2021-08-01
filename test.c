#include <stdio.h>
#include <sys/time.h>

int delaytime(int t) {
        int i, j;
        for (i = 0; i < t; i++)
                for (j = 0; j < 5000; j++);
}

void main() {
        struct timeval tv1, tv2;

        gettimeofday(&tv1, NULL);
        delaytime(100);
        gettimeofday(&tv2, NULL);

        printf("diff: %ldus\n", 1000000 * (tv2.tv_sec - tv1.tv_sec) + (tv2.tv_usec - tv1.tv_usec));
}





