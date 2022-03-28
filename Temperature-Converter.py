#Elements for the choices
list_choices = ['1', '2', '3']
#Elements of Convert Again
yes_no = ['Y', 'N']

#loop menu
while True:
    print("*******Celsius to Fahrenheit Converter*******\n")
    print("Please Select Conversion \n")
    print("1 Celsius to Fahrenheit")
    print("2 Fahrenheit to Celsius")
    print("3 Exit")

#Allow users to input choice   
    choice = input("Enter Choice (1, 2 or 3): ")
 
#Celsius to Fahrenheit Converter
    if choice == '1':
        print("You have chosen to covert from Celsius to Fahrenheit")

#Loop asking for input for invalid values        
        while True:
         
            try:
                input_celsius = input("Please enter temperature in Celsius (°C): ")
                
                if  float(input_celsius) < float(-273.15):
                    print("Nothing can be as cold as or colder than absolute zero. Please input a value greater than or equal to −273.15")
                
                if  float(input_celsius) >= float(-273.15):
                    celsius_to_fahrenheit = ((float(input_celsius) * 9)/5) + 32
                    checker_1 = celsius_to_fahrenheit.is_integer()
                    
                    if checker_1 is True:
                        print(input_celsius,"°C =", int(celsius_to_fahrenheit), "°F")
                        
                        if float(celsius_to_fahrenheit) >= 97 and float(celsius_to_fahrenheit) <= 99:
                            print("Body Temperature")
                            
                        if float(celsius_to_fahrenheit) >= 50 and float(celsius_to_fahrenheit) <=68:
                            print("Cool Day")
                            
                        break
                    if checker_1 is False:
                        round_1 = round(celsius_to_fahrenheit,2)
                        print(input_celsius,"°C =", round_1, "°F")
                        
                        if float(celsius_to_fahrenheit) >= 97 and float(celsius_to_fahrenheit) <= 99:
                           print("Body Temperature") 
                           
                        if float(celsius_to_fahrenheit) >= 50 and float(celsius_to_fahrenheit) <=68:
                           print("Cool Day")
                        
                        break
                    
            except ValueError:
                print("Please enter a Number!")
                
        while True:
            yes_no_input = input("Convert Again? (Y/N): ")
            if yes_no_input not in yes_no:
                print("Invalid Input (Y or N only)")
                
            if yes_no_input == 'N':
                break
            
            if yes_no_input == 'Y':
 
                while True:
                 
                    try:
                        input_celsius = input("Please enter temperature in Celsius (°C): ")
                        
                        if  float(input_celsius) < float(-273.15):
                            print("Nothing can be as cold as or colder than absolute zero. Please input a value greater than or equal to −273.15")
                        
                        if  float(input_celsius) >= float(-273.15):
                            celsius_to_fahrenheit = ((float(input_celsius) * 9)/5) + 32
                            checker_1 = celsius_to_fahrenheit.is_integer()
                            
                            if checker_1 is True:
                                print(input_celsius,"°C =", int(celsius_to_fahrenheit), "°F")
                                
                                if float(celsius_to_fahrenheit) >= 97 and float(celsius_to_fahrenheit) <= 99:
                                    print("Body Temperature")
                                    
                                if float(celsius_to_fahrenheit) >= 50 and float(celsius_to_fahrenheit) <=68:
                                    print("Cool Day")
                                    
                                break
                            if checker_1 is False:
                                round_1 = round(celsius_to_fahrenheit,2)
                                print(input_celsius,"°C =", round_1, "°F")
                                
                                if float(celsius_to_fahrenheit) >= 97 and float(celsius_to_fahrenheit) <= 99:
                                   print("Body Temperature") 
                                   
                                if float(celsius_to_fahrenheit) >= 50 and float(celsius_to_fahrenheit) <=68:
                                   print("Cool Day")
                                
                                break
                            
                    except ValueError:
                        print("Please enter a Number!")

    if choice == '2':
        print("You have chosen to covert from Fahrenheit to Celsius")
        
        while True:
            try:
                input_fahrenheit = input("Please enter temperature in Fahrenheit: ")
                
                if float(input_fahrenheit) < float(-459.67):
                    print("Nothing can be as cold as or colder than absolute zero. Please input a value greater than or equal to −459.67")
                
                if float(input_fahrenheit) >= float(-459.67):
                    fahrenheit_to_celsius = ((float(input_fahrenheit) - 32) * 5)/9
                    checker_2 = fahrenheit_to_celsius.is_integer()
                    
                    if checker_2 is True:
                        print(input_fahrenheit,"°F =", int(fahrenheit_to_celsius), "°C")
                        
                        if float(fahrenheit_to_celsius) >= 36.1 and float(fahrenheit_to_celsius) <= 37.2:
                            print("Body Temperature")
                            
                        if float(fahrenheit_to_celsius) >= 10 and float(fahrenheit_to_celsius) <=20:
                            print("Cool Day")
                        
                        break    
                   
                    if checker_2 is False:
                        round_2 = round(fahrenheit_to_celsius,2)
                        print(input_fahrenheit,"°F =", round_2, "°C")
                        
                        if float(fahrenheit_to_celsius) >= 36.1 and float(fahrenheit_to_celsius) <= 37.2:
                            print("Body Temperature")
                        
                        if float(fahrenheit_to_celsius) >= 10 and float(fahrenheit_to_celsius) <=20:
                            print("Cool Day")
                        
                        break 
                
            except ValueError:
                print("Please enter a Number!")
                
        while True:
            yes_no_input = input("Convert Again? (Y/N): ")
            
            if yes_no_input not in yes_no:
                print("Invalid Input (Y or N only)")            
        
            if yes_no_input == 'N':
                break
            
            if yes_no_input == 'Y':
                
                while True:
                    
                    try:
                        input_fahrenheit = input("Please enter temperature in Fahrenheit: ")
                        
                        if float(input_fahrenheit) < float(-459.67):
                            print("Nothing can be as cold as or colder than absolute zero. Please input a value greater than or equal to −459.67")
                        
                        if float(input_fahrenheit) >= float(-459.67):
                            fahrenheit_to_celsius = ((float(input_fahrenheit) - 32) * 5)/9
                            checker_2 = fahrenheit_to_celsius.is_integer()
                            
                            if checker_2 is True:
                                print(input_fahrenheit,"°F =", int(fahrenheit_to_celsius), "°C")
                                
                                if float(fahrenheit_to_celsius) >= 36.1 and float(fahrenheit_to_celsius) <= 37.2:
                                    print("Body Temperature")
                                    
                                if float(fahrenheit_to_celsius) >= 10 and float(fahrenheit_to_celsius) <=20:
                                    print("Cool Day")
                                
                                break    
                           
                            if checker_2 is False:
                                round_2 = round(fahrenheit_to_celsius,2)
                                print(input_fahrenheit,"°F =", round_2, "°C")
                                
                                if float(fahrenheit_to_celsius) >= 36.1 and float(fahrenheit_to_celsius) <= 37.2:
                                    print("Body Temperature")
                                
                                if float(fahrenheit_to_celsius) >= 10 and float(fahrenheit_to_celsius) <=20:
                                    print("Cool Day")
                                
                                break 
                        
                    except ValueError:
                        print("Please enter a Number!")
                        
    if choice == '3':
        print("Thank you for using my temperature converter!")
        break
    
    if choice not in list_choices:
        print("Please input a valid choice.")