#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <stdbool.h>

#define MAX_FILES 400 //1000
#define MAX_LINES 3000
#define MAX_FILENAME_LENGTH 256
#define MAX_COLS 7
#define MAX_SIZE 15

void replace_last_txt(char *filename) {
    char *last_dot_txt = strrchr(filename, '.'); // Find the last occurrence of '.'
    if (last_dot_txt != NULL && strcmp(last_dot_txt, ".TXT") == 0) {
        strcpy(last_dot_txt, ".txt"); // Replace ".TXT" with ".txt"
    }
}
char initial_file_no[3] = {'0','0','0'};
int result = 0;
char FileNameTempo[MAX_FILENAME_LENGTH];
int main() {
    // Hardcoded directory path
    char path[] = "C:/Users/mcc/Desktop/Internship/file_combine_test/MD13";
    char output_filename[] = "combined_output_md13.txt";
    char filenames[MAX_FILES][MAX_FILENAME_LENGTH];
    char individual_file[MAX_FILENAME_LENGTH];
    char lines[MAX_LINES];
    int file_count = 0;
    struct dirent *entry;
    DIR *dp;

    dp = opendir(path);
    if (dp == NULL) {
        perror("Error opening directory");
        return EXIT_FAILURE;
    }

    printf("Files in the directory '%s':\n", path);
    
    while ((entry = readdir(dp))) {
        if (entry->d_type == DT_REG) {
            strcpy(filenames[file_count], entry->d_name);
            replace_last_txt(filenames[file_count]);
            //printf("%s\n",filenames[file_count]);
            file_count++;
        }
    }
    closedir(dp);
    printf("%d\n",file_count);
    for(int i=0;i<file_count;i++){
        printf("%s\n",filenames[i]);
    }
    FILE *output_file = fopen(output_filename, "w");
    for(int i =0; i <file_count; i++){
        for(int j =0;j<file_count;j++)
        {
            //printf("%s\n",filenames[j]);
            //printf("%c %c %c %c %c %c %c\n ",filenames[j][0],filenames[j][1],filenames[j][2],filenames[j][3],filenames[j][4],filenames[j][5],filenames[j][6]);
            //printf("The initial no is  %d\n",j);
            int result = i; // +1
            if(result <10){
                initial_file_no[0] = result + '0';
                initial_file_no[1] = '.';
                initial_file_no[2] = 't';
            
            }
            else if(result<100){
                initial_file_no[0] = (result/10) + '0';
                initial_file_no[1] = (result%10) + '0';
                initial_file_no[2] = '.';
            }
            else{
                initial_file_no[0] = (result/100) + '0';
                initial_file_no[1] = ((result/10)%10) + '0';
                initial_file_no[2] = (result%10) + '0';
            }

            if(filenames[j][4] == initial_file_no[0] && filenames[j][5] == initial_file_no[1] && filenames[j][6] == initial_file_no[2]){
                printf("The compare result is %s\n",initial_file_no);
                
                snprintf(individual_file, sizeof(individual_file), "%s/%s", path, filenames[j]);
                //printf("the result match is %s\n\n", individual_file);
                FILE *file = fopen(individual_file, "r");
                if (file == NULL) {
                    perror("Error opening file\n");
                    continue;
                }
                else{
                    printf("Reading file: %s\n", individual_file);
                    while (fgets(lines, sizeof(lines), file) != NULL) {
                        fputs(lines, output_file);
                    }
                }
                fclose(file);
            }
            else{
            }

    }
    }
    fclose(output_file);
    printf("Data combined into '%s'\n", output_filename);
    /**/

    return EXIT_SUCCESS;
}
