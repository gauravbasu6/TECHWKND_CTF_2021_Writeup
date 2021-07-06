#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <stdio.h>

struct auth {
  char name[13];
  int id;
};


struct auth *techweekend;
char *service;

void service1(){
  
  printf("%s", THE_FLAG); //THE_FLAG is not the actual flag 
}

int main(int argc, char **argv)
{
  char line[128];

  
  while(1) {
    printf("[ techweekend = %p, service = %p ]\n", techweekend, service);

    if(fgets(line, sizeof(line), stdin) == NULL) break;
    
    if(strncmp(line, "auth ", 5) == 0) {
      techweekend = malloc(8);
      memset(techweekend, 0, 24);
      if(strlen(line + 5) < 10) {
        strcpy(techweekend->name, line + 5);
      }
      else{
        printf("too long");
      }
    }
    if(strncmp(line, "reset", 5) == 0) {
      free(techweekend);
    }
    if(strncmp(line, "service", 6) == 0) {
      service = strdup(line + 7);
    }
    if(strncmp(line, "login", 5) == 0) {
      int *p=techweekend->id;
      printf("the id is %x\n and the pointer is %p\n", techweekend->id,p ); 
      
      if(techweekend->id) {
        service1();
        //printf("you have logged in already!\n");
      } else {
        printf("No entry for you id=0");
      }
    }
  }
}
