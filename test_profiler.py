from profiler import profile_method

@profile_method
def method1():
    return [i**2 for i in range(10000)]

@profile_method
def method2():
    result = []
    for i in range(10000):
        result.append(i**2)
    return result

# Call the methods to see profiling results
method1()
method2()
