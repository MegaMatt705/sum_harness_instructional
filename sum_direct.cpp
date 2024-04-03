// sum_direct.cpp
#include <iostream>
#include <vector>
#include <cstdint>

void setup(int64_t N, uint64_t A[]) {
    std::cout << "Inside direct_sum problem_setup, N=" << N << std::endl;
}

int64_t sum(int64_t N, uint64_t A[]) {
    int64_t sum = 0;
    for (int64_t i = 0; i < N; ++i) {
        sum += A[i];
    }
    return sum;
}
