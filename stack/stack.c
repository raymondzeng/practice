#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include "stack.h"

int main(){
  stack s;
 
  stack_init(&s, 5);

  printf("Pushing 5, 7, 3, 1\n");
  printf("......\n");
  printf("Stack size is %d\n", stack_size(&s));
  stack_push(&s, 1);
  stack_push(&s, 2);
  stack_push(&s, 3);
  stack_push(&s, 4);
  stack_push(&s, 5);
  stack_push(&s, 9);

  printf("The current stack is\n");
  stack_print(&s);
  printf("popped %d\n", stack_pop(&s));
  stack_print(&s);
  
  stack_deallocate(&s);
  stack_print(&s);
  return 0; 
}

void stack_init(stack *s, int capacity){
  (*s).capacity = capacity;
  s->size = 0;
  s->stack = (int *) malloc(s->capacity * sizeof(int));
}

int stack_size(stack *s){
  return s->capacity;
}

// silently ignore pushing to a full stack
void stack_push(stack *s, int e){
  if (s->size == s->capacity) {
    return;
  }
  s->stack[s->size] = e;
  s->size++;
}

int stack_pop(stack *s){
  s->size--;
  return s->stack[s->size];
}

void stack_deallocate(stack *s){
  free(s->stack);
  s->stack = NULL;
  s->size = 0;
}

void stack_print(stack *s){
  for(int i = 0; i < s->size; i++){
    printf("%d\n", s->stack[i]);
  }
}




