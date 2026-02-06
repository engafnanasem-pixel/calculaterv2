history = []
def add_history(text):
    history.append(text)
    if len(history) > 5 :
       history.pop(0)
def add (a, b):
    return a+b ,"😄️"
    
def subtract (a, b):
    return a-b , "🤓️"
   
def multiply (a, b) :
   return a*b , "🤩️"
   
def divide (a, b) :
   if b==0 :
     return None , "🛑️/you can't divide by zero"
   else :
     return a/b , "😉️"

def get_nums():
   try: 
      a = float(input("Enter the first number "))
      b = float (input("Enter the second number"))
      return a, b 
   except ValueError:
      print("❌️ Please Enter VALID number")
      return None  
operations = { "+":add , "-":subtract , "*":multiply , "/":divide }
def main():
   print ("Welcome to the FUN calculater")
   while True :
      print ("\n Choose an option :")
      print ("🎗️ History")
      print ("➕️ ADD")
      print ("➖️ Subtract")
      print ("✖️ Multiply")
      print ("➗️ Divide")
      print ("🧽️ Clear history")
      print ("❌️ exit")
      
      
      choice = input("Your Choice :").lower()
      if choice not in ["+", "-" ,"*","/" ,"exit","history", "clear"] :
         print ("⚠️ Invalid option try again")
         continue
      elif choice == "exit" :
            print ("BYE BYE 👋️")
            break
      elif choice =="history" :
            if not history :
                print("😩️ NO HISTORY ")
            else:
                print("\nCalculation History:")
                for i, h in enumerate(history, start=1):
                   print(f"{i}. {h}")

            continue
      elif choice =="clear" :
            if not history :
                print("🤨️ NO HISTORY to be cleared")
            else:
                history.clear()
                print ("\nThe history is CLEAR 💪️")

            continue
      else:
         
         num1 ,num2 =get_nums()
         func = operations[choice]
         result , emoji = func(num1 , num2)
         if result is None :
            print (emoji)
            continue
         
         
      
      
      operation_txt =f"{emoji} {num1} {choice} {num2} ={result}"
      add_history(operation_txt)
      #print (f"{emoji} The result = {result}")
      print (operation_txt)


main()
      
