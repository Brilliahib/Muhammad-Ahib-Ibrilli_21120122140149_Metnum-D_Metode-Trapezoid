import time

def f(x):
    return 4 / (1 + x**2)

def reimann_integral(N):
    delta_x = 1 / N
    sum_result = sum(f(delta_x * (i + 0.5)) for i in range(N))
    return delta_x * sum_result

def rms_error(approximation):
    return abs(approximation - pi_reference)

def test_integration(N_values):
    for N in N_values:
        start_time = time.time()
        approximation = reimann_integral(N)
        execution_time = time.time() - start_time
        error = rms_error(approximation)
        print(f"N = {N}, Approximation = {approximation}, RMS Error = {error}, Execution Time = {execution_time}")

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Pengujian
test_integration(N_values)