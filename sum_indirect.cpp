#include <iostream>
#include <vector>
#include <cstdint>
#include <cstdio> // For printf
#include <cstdlib> // For std::rand and std::srand
#include <ctime> // For std::time

void setup(int64_t N, uint64_t A[]) {
    printf("Inside sum_indirect problem_setup, N=%lld\n", N);
    std::srand(std::time(0)); // Seed the random number generator
    for (int64_t i = 0; i < N; ++i) {
        A[i] = std::rand() % N; // Generate a random number in the range 0 to N-1
    }
}

int64_t sum(int64_t N, uint64_t A[]) {
    printf("Inside sum_indirect perform_sum, N=%lld\n", N);
    int64_t sum = 0;
    for (int64_t i = 0; i < N; ++i) {
        sum += A[i];
    }
    return sum;
}
