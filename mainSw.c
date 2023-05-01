#include <stdio.h>
#include <stdlib.h>
#include "local_align.h"


int main()
{

    char X[] = "GGCTCAATCA";
    char Y[] = "ACCTAAGG";
    int match = 2;
    int mismatch = -1;
    int gap = -2;

    printf("Generating output matrix...\n");

    local_alignment_info* info =
                (local_alignment_info*)malloc(sizeof(local_alignment_info));


    local_align_construct(info, X, Y, match, mismatch, gap);

    printf("max score = %d in coordinates(%d,%d)\n\n", info->score,
                                            info->score_n, info->score_m);
    printf("Score Matrix:\n");

    draw_mat(info, X, Y, 1);

    printf("Direction Matrix:\n");

    draw_mat(info, X, Y, 0);

    printf("Generating traceback...\n");

    print_local_align_trace_back(info,X,Y);

    printf("Done, deleting garbage...\n");

    delete_local_alignment_info(info);

    printf("Success\n");

    return 0;

}
