#include "local_align.h"

int max_non_neg(int a, int b, int c){

    int max_temp = (a > b) ? a : b;
    max_temp = (max_temp > c) ? max_temp : c;
    return (max_temp  > 0) ? max_temp : 0;
}

void local_align_construct(         local_alignment_info* loc_align_info_temp,
                                    char* X, char* Y, int match_score,
                                    int mismatch_score, int gap_penalty
                                    ){

    int n = strlen(X);
    int m = strlen(Y);
    int max_score = 0;

    int **score_mat_temp = (int **) calloc(m+1, sizeof(int *));
    for (int i = 0; i < m+1; i++)
        score_mat_temp[i] = (int *) calloc(n+1, sizeof(int));

    int **align_mat_temp = (int **) calloc(m+1, sizeof(int *));
    for (int i = 0; i < m+1; i++)
        align_mat_temp[i] = (int *) calloc(n+1, sizeof(int));

    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            int match = (X[j-1] == Y[i-1]) ? match_score : mismatch_score;
            int diagonal_score = score_mat_temp[i-1][j-1] + match;
            int up_score = score_mat_temp[i-1][j] + gap_penalty;
            int left_score = score_mat_temp[i][j-1] + gap_penalty;

            score_mat_temp[i][j] = max_non_neg(diagonal_score,
                                                up_score, left_score);
            //diagonal=0 up=1 left=2
            if(score_mat_temp[i][j] == diagonal_score)
                align_mat_temp[i][j] = 0;
            else if(score_mat_temp[i][j] == up_score)
                align_mat_temp[i][j] = 1;
            else
                align_mat_temp[i][j] = 2;

            if(score_mat_temp[i][j] > max_score){
                max_score = score_mat_temp[i][j];
                loc_align_info_temp->score_m = i+1;
                loc_align_info_temp->score_n = j+1;
            }
        }
    }

    loc_align_info_temp->m = m;
    loc_align_info_temp->n = n;
    loc_align_info_temp->score_mat = score_mat_temp;
    loc_align_info_temp->alignment_mat = align_mat_temp;
    loc_align_info_temp->score = max_score;

}

void draw_mat(local_alignment_info *loc_align_info, char* X, char* Y, int num){

    int **matrix = (num==1) ? loc_align_info->score_mat :
                                        loc_align_info->alignment_mat;
    int m = loc_align_info->m;
    int n = loc_align_info->n;

    printf("    ");
    for (int j = 0; j < n+1; j++) {
            printf(" %c ", X[j-1]);
    }
    printf("\n");

    for (int i = 0; i < m+1; i++) {
        if(i!=0) printf(" %c ", Y[i-1]);
        else printf("   ", Y[i]);
        for (int j = 0; j < n+1; j++) {
            printf(" %d ", matrix[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void delete_local_alignment_info(local_alignment_info *loc_align_info_temp){
    free(loc_align_info_temp->score_mat);
    free(loc_align_info_temp->alignment_mat);
    free(loc_align_info_temp);
}

void print_local_align_trace_back(local_alignment_info *loc_align_info_temp,
                            char* X, char* Y){

    int **score_mat = loc_align_info_temp->score_mat;
    int **align_mat = loc_align_info_temp->alignment_mat;

    int m = loc_align_info_temp->score_m - 1;
    int n = loc_align_info_temp->score_n - 1;

    int Y_len = loc_align_info_temp->m;
    int X_len = loc_align_info_temp->n;
    int out_idx = (X_len>Y_len) ? X_len : Y_len;
    char *X_out = (char*)calloc(out_idx, sizeof(char));
    char *Y_out = (char*)calloc(out_idx, sizeof(char));
    int iterator = out_idx;

    while( m>0 && n>0 && score_mat[m][n]!=0){

        switch (align_mat[m][n]){

        case 0://diagonal

            X_out[iterator-1] = X[n-1];
            Y_out[iterator-1] = Y[m-1];

            m = m-1;
            n = n-1;

            break;

        case 1://up

            X_out[iterator-1] = '-';
            Y_out[iterator-1] = Y[m-1];

            m = m-1;
            break;

        case 2:

            X_out[iterator-1] = X[n-1];
            Y_out[iterator-1] = '-';

            n = n-1;

            break;
        }
        iterator = iterator - 1;
    }

    int start = out_idx - iterator;

    printf("X=");
    for (int i = start-1; i < out_idx; i++) {
        printf(" %c", X_out[i]);
    }
    printf("\nY=");
    for (int i = start-1; i < out_idx; i++) {
        printf(" %c", Y_out[i]);
    }
    printf("\n\n");

    free(X_out);
    free(Y_out);
}
