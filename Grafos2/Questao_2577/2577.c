typedef struct {
    int time, x, y;
} Node;

Node* heap;
int heapSize = 0;

void push(Node node) {
    int i = heapSize++;
    while (i > 0) {
        int p = (i - 1) / 2;
        if (heap[p].time <= node.time) break;
        heap[i] = heap[p];
        i = p;
    }
    heap[i] = node;
}

Node pop() {
    Node res = heap[0];
    Node last = heap[--heapSize];
    int i = 0;
    while (i * 2 + 1 < heapSize) {
        int a = i * 2 + 1, b = i * 2 + 2, min = a;
        if (b < heapSize && heap[b].time < heap[a].time) min = b;
        if (heap[min].time >= last.time) break;
        heap[i] = heap[min];
        i = min;
    }
    heap[i] = last;
    return res;
}

int minimumTime(int** grid, int gridSize, int* gridColSize) {
    int m = gridSize, n = gridColSize[0];
    if (grid[0][1] > 1 && grid[1][0] > 1) return -1;

    bool** visited = malloc(m * sizeof(bool*));
    for (int i = 0; i < m; i++) {
        visited[i] = calloc(n, sizeof(bool));
    }

    heap = malloc(sizeof(Node) * m * n * 4);
    heapSize = 0;

    push((Node){0, 0, 0});

    int dirs[4][2] = {{0,1}, {1,0}, {0,-1}, {-1,0}};

    while (heapSize > 0) {
        Node cur = pop();

        int t = cur.time, x = cur.x, y = cur.y;

        if (visited[x][y]) continue;

        visited[x][y] = true;

        if (x == m - 1 && y == n - 1)
            return t;

        for (int d = 0; d < 4; d++) {
            int nx = x + dirs[d][0], ny = y + dirs[d][1];
            if (nx < 0 || ny < 0 || nx >= m || ny >= n || visited[nx][ny]) continue;

            int arrive = t + 1;
            int ready = grid[nx][ny];

            if (arrive < ready) {
                int wait = ready;
                if ((wait % 2) != (arrive % 2)) wait++;
                arrive = wait;
            }

            push((Node){arrive, nx, ny});
        }
    }

    return -1;
}
