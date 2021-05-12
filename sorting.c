#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void main () {
    int arr[7]={24,25,23,27,22,28,26};
    int idp = fork();

    if (idp == 0){
        printf(" ");
    }
    else {
        for(int i=0;i<6;i++){
        for(int j=0;j<6;j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
            }}

        printf("\nParent Process Sorting Array in Ascending Order: [  ");
    }
    for(int i=0;i<6;i++){
            printf("%d  ",arr[i]);}
        printf("]\n");
}