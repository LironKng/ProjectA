#ifndef LOCAL_ALIGN_H_INCLUDED
#define LOCAL_ALIGN_H_INCLUDED

#define ZERO 0

typedef struct {
    int **score_mat;
    int **alignment_mat;
    int m;
    int n;
    int score;
    int score_m;
    int score_n;

} local_alignment_info;

//find the maximum of a,b,c
int max_non_neg(int a, int b, int c);

//fill the local_alignment_info struct
//need to free the returned struct
void local_align_construct(         local_alignment_info *loc_align_info_temp,
                                    char* X, char* Y, int match_score,
                                    int mismatch_score, int gap_penalty);

void print_local_align_trace_back(local_alignment_info *loc_align_info_temp,
                            char* X, char* Y);

void draw_mat(local_alignment_info *loc_align_info, char* X, char* Y,
                                        int num);//1-score 2-alignment

void delete_local_alignment_info(local_alignment_info *loc_align_info_temp);

#endif // LOCAL_ALIGN_H_INCLUDED
