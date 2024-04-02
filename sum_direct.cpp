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

// benchmark.cpp
#include <iostream>
#include <chrono>
#include "sum_direct.h"

void benchmark_sum(int64_t N, uint64_t A[]) {
    std::cout << "Benchmarking sum function...\n";

    // Start the timer
    std::chrono::time_point<std::chrono::high_resolution_clock> start_time = std::chrono::high_resolution_clock::now();

    // Call the sum function
    int64_t result = sum(N, A);

    // Stop the timer
    std::chrono::time_point<std::chrono::high_resolution_clock> end_time = std::chrono::high_resolution_clock::now();

    // Calculate the elapsed time
    std::chrono::duration<double> elapsed = end_time - start_time;

    // Report the result and elapsed time
    std::cout << "Sum: " << result << "\n";
    std::cout << "Elapsed time: " << elapsed.count() << " seconds\n";
}

int main() {
    int64_t N = 1000000; // Example size
    std::vector<uint64_t> A(N, 1); // Example array filled with 1s

    benchmark_sum(N, A.data());

    return 0;
}
