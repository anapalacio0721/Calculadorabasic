class Calculator:
    def __init__(self,a,b,result):
        self.a= a
        self.b= b
        self.result= result

    def get_addition(self,a,b):
        print("ingresar numero: " + str(a))
        print("ingresar numero: " + str(b))
        self.result = a + b
        print("The result of addition is " + str(self.result))

    def get_sustraction(self,a,b):
        print("ingresar numero: " + str(a))
        print("ingresar numero: " + str(b))
        self.result = a - b
        print("The result of sustraction is " + str(self.result))

    def get_multiplication(self):
        print("ingresar numero: " + str(a))
        print("ingresar numero: " + str(b))
        self.result = a * b
        print("The result of multiplication is " + self.result)

    def get_divition(self):
        print("ingresar numero: " + str(a))
        print("ingresar numero: " + str(b))
        self.result = a / b
        print("The result of divition is " + self.result)

    def get_square_circle(self):
        print("The result of square_circle is " + self.result)
        

def main():
    calculadora =Calculator(3,1,0)
    print("el resultado de la suma")
    calculadora.get_addition(3,4)
    print("el resultado de la resta ")
    calculadora.get_sustraction(3,4)
    
     
               

if __name__ == "__main__":
    main()
