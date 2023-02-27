#include <stdio.h>

// Função que calcula o fatorial de um número
int fatorial(int num) {
  if (num <= 1) {
    return 1;
  } else {
    return num * fatorial(num-1);
  }
}

// Função que calcula o arranjo de n elementos tomados k a k
int arranjo(int n, int k) {
  return fatorial(n) / fatorial(n-k);
}

// Função que calcula a permutação de n elementos
int permutacao(int n) {
  return fatorial(n);
}

// Função que calcula a combinação de n elementos tomados k a k
int combinacao(int n, int k) {
  return fatorial(n) / (fatorial(k) * fatorial(n-k));
}

// Função principal
int main() {
  int n, k;

  printf("Digite o valor de n: ");
  scanf("%d", &n);

  printf("Digite o valor de k: ");
  scanf("%d", &k);

  printf("\nArranjo de %d elementos tomados %d a %d: %d\n", n, k, k, arranjo(n, k));
  printf("Permutação de %d elementos: %d\n", n, permutacao(n));
  printf("Combinação de %d elementos tomados %d a %d: %d\n", n, k, k, combinacao(n, k));

  return 0;
}
