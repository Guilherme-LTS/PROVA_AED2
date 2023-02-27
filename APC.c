#include <stdio.h>

int arranjo(int n, int p) {
    int resultado = 1;
    for (int i = 0; i < p; i++) {
        resultado *= (n - i);
    }
    return resultado;
}

int permutacao(int n) {
    int resultado = 1;
    for (int i = 1; i <= n; i++) {
        resultado *= i;
    }
    return resultado;
}

int combinacao(int n, int p) {
    if (p == 0 || p == n) {
        return 1;
    } else {
        return combinacao(n - 1, p - 1) + combinacao(n - 1, p);
    }
}

int main() {
    int n = 5;
    int p = 10;

    printf("Arranjo de %d elementos tomados %d a %d: %d\n", n, p, p, arranjo(n, p));
    printf("Permutação de %d elementos: %d\n", n, permutacao(n));
    printf("Combinação de %d elementos tomados %d a %d: %d\n", n, p, p, combinacao(n, p));

    return 0;
}
