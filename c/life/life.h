int is_alive(int *state, int len, int height, int width, int index);

int count_alive_neighbors(int *state, int len, int height, int width, int row, int col);

void update(int *curr, int *next, int len, int height, int width);

void set_alive(int *state, int index);

void set_dead(int *state, int index);
