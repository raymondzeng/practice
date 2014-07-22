
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

