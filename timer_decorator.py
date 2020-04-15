import random
import time


def timerfunc(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = f"The runtime for {func.__name__} took {runtime} seconds to complete"
        print(msg)
        return value

    return function_timer


@timerfunc
def long_runner():
    for x in range(2):
        sleep_time = random.choice(range(2))
        time.sleep(sleep_time)


if __name__ == '__main__':
    long_runner()