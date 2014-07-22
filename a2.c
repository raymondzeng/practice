#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

struct stack{
  int size;
  int capacity;
  int *stack;
};

typedef struct stack my_stack;

void stack_init(my_stack *s, int capacity);
void stack_print(my_stack *s);
void stack_push(my_stack *s, int e);
int stack_size(my_stack *s);
int stack_pop(my_stack *s);
void stack_deallocate(my_stack *s);

int main(){
  my_stack s;
  
  stack_init(&s, 5);
  printf("Pushing 5, 7, 3, 1\n");
  printf("......\n");
  printf("Stack size is %d\n", stack_size(&s));
  stack_push(&s, 5);
  stack_push(&s, 7);
  stack_push(&s, 3);
  stack_push(&s, 1);
  printf("The current stack is\n");
  stack_print(&s);
  printf("popped %d\n", stack_pop(&s));
  stack_print(&s);
  
  stack_deallocate(&s);
  stack_print(&s);
  return 0; 
}

void stack_init(my_stack *s, int capacity){
  (*s).capacity = capacity;
  s->size = 0;
  s->stack = (int *) malloc(s->size * sizeof(int));
  
}

int stack_size(my_stack *s){
  return s->size;
}
void stack_push(my_stack *s, int e){
  s->stack[s->size] = e;
  s->size++;
  
}
int stack_pop(my_stack *s){
  s->size--;
  return s->stack[s->size];
}

void stack_deallocate(my_stack *s){
  free(s);
}

void stack_print(my_stack *s){
  for(int i = 0; i < s->size; i++){
    printf("%d\n", s->stack[i]);
  }
}




