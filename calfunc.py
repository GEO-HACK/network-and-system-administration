def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y == 0 :
        raise ValueError("cannot divide by zero.")
    return x / y
    
def calculator():
    
    while True:
        try:
   
           num1 = (float(input("ENter the first number:")))
           num2 = (float(input("ENter the second number:")))
           print("1.Addition\n" "2.subtraction\n" "3.multiplication\n" "4.division\n" "5.exit\n")
           choice=(str(input("choose operation (use 1/2/3/4/5):")))

        
           if choice == '5':
             break
           elif choice == '1':
            result = add(num1,num2)
           elif choice == '2':
            result = subtract(num1,num2)
           elif choice == '3':
            result= multiply(num1,num2)
           elif choice == '4':
            result=divide(num1,num2)
        
        
           print("result:{}".format(result))
           
        except ValueError as e:
            print('error',e)
        except Exception as e:
            print("An error occurred",e)
            
        finally:
            another_calculation = input("DO you want to perform another calculation?(y/n): ")
            if another_calculation != 'y':
                print("Exitng the calculator . GOodbye!")   
                break
if __name__ == "__main__":
    calculator()                   
        
        
                    
    
    

