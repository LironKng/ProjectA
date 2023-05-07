#include "local_align.h"


int main(int argc, char *argv[])
{

    if(argc < 2){
            printf("too few arguments: <seq1> <seq2> is missing\n");
            return -1;
    }

    int print_out = 1;

    if(argc > 3)
        if(!strcmp(argv[3], "-q")){
                        print_out = 0;
        }

    char *X = argv[1];
    char *Y = argv[2];
    int match = 2;
    int mismatch = -1;
    int gap = -2;

    if(print_out)
        printf("Generating output matrix...\n");

    local_alignment_info* info =
                (local_alignment_info*)malloc(sizeof(local_alignment_info));


    local_align_construct(info, X, Y, match, mismatch, gap);

    if(print_out){
        printf("max score = %d in coordinates(%d,%d)\n\n", info->score,
                                                info->score_n, info->score_m);
        printf("Score Matrix:\n");

        draw_mat(info, X, Y, 1);

        printf("Direction Matrix:\n");

        draw_mat(info, X, Y, 0);

        printf("Generating traceback...\n");

        print_local_align_trace_back(info,X,Y);

        printf("Done, deleting garbage...\n");
    }

    delete_local_alignment_info(info);

    printf("C implementation success\n");

    return 0;

}
