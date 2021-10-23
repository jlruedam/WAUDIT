print("Introducción:")

print("El numero octal 0o123 -> es en decimal:",0o123)
print("El número hexadecimal 0x123 -> es decimal:",0x123)


print("Flotantes y Notación científica:")
print("El número 3e8 es igual a:", 3e18)
print(0.0000000000000000000001)
print(1e-22)

#######################
print("----Otras formas de conversión----")

print("Conversión binario a decimal:")
num="1010"
print(f"El número binario {num} es", int(num,2),"en decimal")
print()

print("Conversion de deimal a binario: ")
num=10
print(f"El número decimal {num} es", bin(num),"en binario")
print()


print("Conversión octal a decimal:")
num="1237"
print(f"El número octal {num} es", int(num,8),"en decimal")
print()

print("Conversión decimal a octal:")
num=1237
print(f"El número decimal {num} es", oct(num),"en octal")
print()



print("Conversión hexadecimal a decimal:")
num="123A"
print(f"El número hexadecimal {num} es", int(num,16),"en decimal")
print()

print("Conversión decimal a Hexadecimal:")
num=1237
print(f"El número hexadecimal {num} es", hex(num),"en hexadecimal")
print()
