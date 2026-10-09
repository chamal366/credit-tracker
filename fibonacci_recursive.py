def fib_sequence(n):
    """Return the Fibonacci sequence up to n terms using recursion.

    Args:
        n (int): number of terms (non-negative)

    Returns:
        list: Fibonacci sequence as a list of integers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    seq = fib_sequence(n - 1)
    seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    try:
        n = int(input("Enter n (positive integer): "))
    except Exception:
        print("Invalid input; please enter a positive integer.")
    else:
        print(f"Fibonacci sequence up to {n} terms:")
        print(fib_sequence(n))
