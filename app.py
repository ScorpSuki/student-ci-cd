def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Тек сан болуы қажет")
    return a + b

if __name__ == "__main__":
    print("Нәтиже:", add(2, 3))
