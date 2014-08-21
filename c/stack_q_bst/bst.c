#include <stdio.h>

struct bst {
  int key;
  struct bst* left;
  struct bst* right;
};

typedef struct bst bst;

bst* search(bst *tree, int key);
bst* search(bst *tree, int key) {
  if (tree == NULL) {
    return NULL;
  }

  if (tree->key == key) 
    return tree;
  else if (tree->key > key) {
    return search(tree->left, key);
  } else {
    return search(tree->right, key);
  }
}

void insert(bst **tree, int key);
void insert(bst **tree, int key) {
  if (tree == NULL) {
    printf("**tree is null; doing nothing\n");
    return;
  }
  
  if (*tree == NULL) {
    printf("pointer points to null pointer\n");
    bst n;
    n.key = key;
    n.left = NULL;
    n.right = NULL;
    *tree = &n;
    return;
  }
  
  printf("pointer points to pointer to bst\n");
  bst* t = *tree;
  if (t->key > key) {
    insert(&(t->left), key);
  } else {
    insert(&(t->right), key);
  }
}

int main() {
  bst t;
  t.key = 1;
  t.left = NULL;
  t.right = NULL;
  bst* p = &t;
  insert(&p, 3);
  printf("%d\n", p->right->key);
  bst* found = search(p, 3);
  printf("%p\n", found);
}
