
# import art
# print(art.logo)

#Adding
def add (n1, n2):
    return n1 + n2

#Substract
def sub (n1, n2):
    return n1 - n2

#Multiply
def mult (n1, n2):
    return n1 * n2

#Division
def div (n1, n2):
    if n2 == 0:
        return "syntax error"
    return n1 / n2

#Hashmap operations
operations = {
    "+" : add,
    "-" : sub,
    "*" : mult,
    "/" : div, 
}

num1 = int(input("First number:"))
num2 = int(input("First number:"))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above:")
calculation_function = operations[operation_symbol] #utilizamos el input de simbolos, y lo pasamos como llave para sacar el value
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")