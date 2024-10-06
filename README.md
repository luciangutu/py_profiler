# Python Profiler

This is a lightweight Python profiler that measures the execution time, memory usage, and CPU usage of a function. It can be used to optimize code performance by identifying resource-intensive functions.
This profiler is suitable for small functions. For more extensive profiling, consider using more comprehensive profiling tools.

## Features

- **Time Profiling:** Measures the elapsed time for a function to execute.
- **Memory Profiling:** Tracks memory usage before and after function execution.
- **CPU Profiling:** Monitors CPU usage during function execution.

## Installation

You need to have the following packages installed:

- `memory_profiler`
- `psutil`

You can install them using pip:

```bash
pip install -r requirements.in
```


## Usage
To use the profiler, simply decorate the function you want to profile with the @profile_method decorator.

## Example
```python
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
```


