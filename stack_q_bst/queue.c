#include <stdlib.h>

struct queue {
  int size;
  int capacity;
  int * queue;
};

typedef struct queue queue;

void queue_init(queue *q, int cap);
int queue_size(queue *q);
int queue_dequeue(queue *q);
void queue_enqueue(queue *q, int e);
void queue_deallocate(queue *q);

void queue_init(queue *q, int capacity) {
  q->capacity = capacity;
  q->size = 0;
  q->queue = (int *) malloc(q->capacity * sizeof(int));
}

int queue_size(queue *q) {
  return q->size;
}

int queue_dequeue(queue *q) {
  /* if (q->size == 0) { */
  /*   //return undefined; */
  /*   // TODO how do ?? */
  /* } */
  int elem = *(q->queue);
  q->queue++;
  q->size--;
  return elem;
}

void queue_enqueue(queue *s, int e) {
  if (s->capacity == s->size) {
    return;
  }
  s->queue[s->size] = e;
  s->size++;
}

void queue_deallocate(queue *s) {
  free(s->queue);
  s->queue = NULL;
  s->size = 0;
}


int main() {
}

