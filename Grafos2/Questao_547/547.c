int find(int* parent, int i) {
    if (parent[i] != i)
        parent[i] = find(parent, parent[i]);
    return parent[i];
}

void unite(int* parent, int* rank, int x, int y) {
    int rootX = find(parent, x);
    int rootY = find(parent, y);

    if (rootX != rootY) {
        if (rank[rootX] > rank[rootY]) {
            parent[rootY] = rootX;
        } else if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else {
            parent[rootY] = rootX;
            rank[rootX]++;
        }
    }
}

int findCircleNum(int** isConnected, int isConnectedSize, int* isConnectedColSize) {
    int parent[isConnectedSize];
    int rank[isConnectedSize];

    for (int i = 0; i < isConnectedSize; i++) {
        parent[i] = i;
        rank[i] = 0;
    }

    for (int i = 0; i < isConnectedSize; i++) {
        for (int j = 0; j < isConnectedSize; j++) {
            if (isConnected[i][j] == 1) {
                unite(parent, rank, i, j);
            }
        }
    }

    int provinces = 0;
    for (int i = 0; i < isConnectedSize; i++) {
        if (parent[i] == i) {
            provinces++;
        }
    }

    return provinces;
}