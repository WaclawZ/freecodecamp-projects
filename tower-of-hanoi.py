def hanoi_solver(num: int) -> str:
    first = [n for n in range(num, 0, -1)]
    second, third = [], []

    steps = []

    def record_state():
        steps.append(f"{first} {second} {third}")

    record_state()

    def move(n, source, target, temp):
        if n > 0:
            move(n - 1, source, temp, target)
            target.append(source.pop())
            record_state()
            move(n - 1, temp, target, source)

    move(num, first, third, second)

    return "\n".join(steps)
