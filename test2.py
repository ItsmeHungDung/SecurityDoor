import u3
from time import sleep
dev=u3.U3()

button1_port=0 #AIN0
button2_port=1 #AIN1
button3_port=2 #AIN2
button4_port=3 #AIN3

fio4_port = 4 #FIO4
fio5_port = 5 #FIO5
fio6_port = 6 #FIO6 
fio7_port = 7 #FIO7

dac0_port = 0 #DAC0
dac1_port = 1 #DAC1

#frequency_hz = 1000  # 1 kHz
#duty_cycle = 0.8  # 20%
#time_period = 1 / frequency_hz
#on_time = duty_cycle * time_period
#off_time = time_period - on_time

try:
    while True:
        
        #Button 1 use for locking the door.
        button1=dev.getAIN(button1_port)
        button2=dev.getAIN(button2_port)
        button3=dev.getAIN(button3_port)
        button4=dev.getAIN(button4_port)
        print(f"Voltage Button 1: {button1}")
        if button1 > 4.0:
            dev.writeRegister(fio4_port + 6000, 1)
            print(f"Button 1 is pressed, Opening the Door!")
        else:
            dev.writeRegister(fio4_port + 6000, 0)
            
        #Button 2 use for control the speed of the door.
        print(f"Voltage Button 2: {button2}")
        if button2 > 4.0:
            #frequency_hz = 1000  # 1 kHz
            #duty_cycle = 0.2  # 20%
            #time_period = 1 / frequency_hz
            #on_time = duty_cycle * time_period
            #off_time = time_period - on_time
            #print("Set up the door to open and close faster")
            #dev.writeRegister(fio6_port+6000,1)
            #print("Button 1 pressed")
            dev.writeRegister(fio5_port + 6000, 1)
            print(f"Button 2 is pressed, Closing the Door!")
        else:
            #frequency_hz = 1000  # 1 kHz
            #duty_cycle = 0.8  # 80%
            #time_period = 1 / frequency_hz
            #on_time = duty_cycle * time_period
            #off_time = time_period - on_time
            #print("Set up the door to open and close slower")
            dev.writeRegister(fio5_port + 6000, 0)

        #Button 3 open for the door and close the door 
        
        print(f"Voltage Button 3: {button3}")
        while button3 > 4.0:
            print(f"The door has been locked, contact the admin to open the door")
            button3=dev.getAIN(button3_port)
            dev.writeRegister(fio4_port + 6000, 0)
            dev.writeRegister(fio5_port + 6000, 0)
            sleep(0.1)

        sleep(0.1)
except KeyboardInterrupt:
    print("\nExiting the program")
finally:
    dev.close()
