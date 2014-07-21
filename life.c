#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

void print_arr(int *arr, int len, int height, int width) {
  // print the board
  for (int i = 0; i < len; i++) {
    printf("%2d ", arr[i]);
    // if end of row, put new line
    if (i % width == (width - 1)) {
      printf("\n");
    }
  }
}

int get_index(int height, int width, int row, int col) {
  return width * row + col;
}

int main() {
  int height = 5;
  int width = 4;
  int len = height * width;
  int board[len];


  // init random generator
  srand(time(NULL));

  // init the board  
  for (int i = 0; i < len; i++) {
    // randomly pick between 0 and 1
    int r = round(rand() % 2);
    board[i] = r;
  }  

  print_arr(board, len, height, width);

  int idx = get_index(height, width, 3, 2);
  printf("%d %d\n", idx, board[idx]);
  return 0;
}
