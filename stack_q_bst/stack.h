
struct stack{
  int size;
  int capacity;
  int *stack;
};

typedef struct stack stack;

void stack_init(stack *s, int capacity);
void stack_print(stack *s);
void stack_push(stack *s, int e);
int stack_size(stack *s);
int stack_pop(stack *s);
void stack_deallocate(stack *s);

