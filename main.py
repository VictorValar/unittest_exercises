def avg(*args:float) -> float:
    total = 0
    for num in args:
        total += num
    return total / len(args)


def counter(name: str) -> int:
    return len(name)

