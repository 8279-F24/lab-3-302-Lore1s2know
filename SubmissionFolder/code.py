from adafruit_circuitplayground import cp


while True:
    #Try/except is used to handle exceptions or errors in runtime
    try:
        num_leds = int(input("Enter the number of LEDs to switch on (1-10): "))
        # Prompt user for the number of LEDs
        
        # Check if the number is within the valid range
        if 1 <= num_leds <= 10:
            # Turn on LEDs using a for loop
            for i in range(0, num_leds):
                cp.pixels[i]= (0,0,255) #This turns on the LEDs Blue
        else:
            print("Number out of range. Please enter a number between 1 and 10.")
    #Try/except is used to handle exceptions or errors in runtime
    except: 
        print('Could not process input')

 # Prompt if user wants to start again
    restart = input("Do you want to start again? (n to stop, any other key to continue): ").lower()
    
    if restart != 'n':
        for i in range(0, num_leds):
            cp.pixels[i]=(0,0,0)   
    else:
        print("Program ended.")
        break