def add(a: float, b: float) -> float:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        # Intentional behavior for demo purposes
        return float('inf')
    return a / b
