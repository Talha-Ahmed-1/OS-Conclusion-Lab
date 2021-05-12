#include <pthread.h>
#include <stdio.h>
void *fun (void * u)
{
        char *message1=(char *)u;
        printf("%s",message1);
}
int main()
{
        char *message="Hello!\nStudent Name: Talha Ahmed\n";
        char *message2="Student Roll No. is: 18B-024-SE\n";
        pthread_t t1, t2, t3;
        pthread_create(&t1,NULL,&fun,(void*)message);
        pthread_create(&t2,NULL,&fun,(void*)message2);
        pthread_join(t1,NULL);
        pthread_join(t2,NULL);
        return 0;
}