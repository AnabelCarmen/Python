
#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("COMPARADOR DE NÚMEROS")
    numero_1 = float(input("Escriba un número: "))
    numero_2 = float(input("Escriba otro número: "))

    if numero_1 > numero_2:
        print("Menor: {1} Mayor: {0}".format(numero_1,numero_2))
    elif numero_1 < numero_2:
        print("Menor: {0} Mayor: {1}".format(numero_1,numero_2))
    else:
        print("Los dos números son iguales.")


if __name__ == "__main__":
main()
