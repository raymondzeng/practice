#include <time.h>
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

// headers
int is_alive(int *state, int len, int height, int width, int index);
int count_alive_neighbors(int *state, int len, int height, int width, int row, int col);
void update(int *curr, int *next, int len, int height, int width);

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
  if (row < 0 || col < 0) {
    return -1;
  }
  return width * row + col;
}

void do_life(int *start_state, int len, int height, int width, int life_cycles){
  int *current_state = start_state;

  while(life_cycles--){
    int next_state[len];
    update(current_state, next_state, len, height, width);
    print_arr(current_state, len, height, width);
    current_state = next_state;
  }
}

int is_in_range(int len, int index){
  return index >= 0 && index < len;
}

void update(int *current_state, int *next_state, int len, int height, int width){
  for (int i = 0; i < len; i++) {
    int row = i / width;
    int col = i % width;
    int live_neighbours = count_alive_neighbors(current_state, len, height, width, row, col);
    printf("%d neighbours\n", live_neighbours);

    // TODO : cases for num of live neighbors
  }
}

void set_alive(int *arr, int index) {
  arr[index] = 1;
}

void set_dead(int *arr, int index) {
  arr[index] = 0;
}

int count_alive_neighbors(int *state, int len, int height, int width, int row, int col) {
  int row_offset[3] = {0,1,-1};
  int col_offset[3] = {0,1,-1};

  int sum = 0;
  for (int i = 0; i < 3; i++) {
    for (int j = 0; j < 3; j++) {
      if (i == 0 && j == 0) {
        continue;
      }      
      int index = get_index(height, width, row + row_offset[i], col + col_offset[j]);
      sum += is_alive(state, len, height, width, index);
    }
  }  
  return sum;
}

int is_alive(int *state, int len, int height, int width, int index) {
  if (is_in_range(len, index)) {
    return state[index];
  }
  return 0;
}

int main() {
  int height = 4;
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
  printf("%d\n", count_alive_neighbors(board, len, height, width, 0, 0));
  //  do_life(board, len, height, width, 1);

  return 0;
}
