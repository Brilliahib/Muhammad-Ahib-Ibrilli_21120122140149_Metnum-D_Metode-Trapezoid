import time

def f(x):
    return 4 / (1 + x**2)

def trapezoidal_integration(a, b, N):
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        integral += f(a + i * h)
    integral *= h
    return integral

def calculate_pi(N):
    return trapezoidal_integration(0, 1, N)

def rms_error(approx, exact):
    return ((approx - exact) ** 2) ** 0.5

def main():
    exact_pi = 3.14159265358979323846
    N_values = [10, 100, 1000, 10000]

    print("N\tApproximation\tRMS Error\tExecution Time")
    for N in N_values:
        start_time = time.time()
        approx_pi = calculate_pi(N)
        execution_time = time.time() - start_time
        error = rms_error(approx_pi, exact_pi)
        print(f"{N}\t{approx_pi}\t{error}\t{execution_time}")

if __name__ == "__main__":
    main()
