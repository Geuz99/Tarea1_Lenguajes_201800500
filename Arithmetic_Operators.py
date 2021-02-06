if __name__ == '__main__':
    a = int(input())
    b = int(input())

    def sum(a,b):
        suma = a + b
        return suma

    def diff(a,b):
        resta = a - b
        return resta

    def product(a,b):
        multiplicacion = a * b
        return multiplicacion

    print(sum(a,b))
    print(diff(a,b))
    print(product(a,b))
