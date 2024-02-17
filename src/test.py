import serial
import time

if __name__ == "__main__":
    # Parameters for serial port
    serial_port = 'COM3'  
    baud_rate = 115200
    
    # Opens serial port
    ser = serial.Serial(serial_port, baud_rate, timeout=0.5)
    
    # Writes a soft reset string (Ctrl+D, essentially)
#     ser.write(b'\x04')
    
    inp = input("Set ur gain: ") + '\r\n'
    ser.write(inp.encode())

    # Variables used for while loop
    end_cond = 0
    x_values = []
    y_values = []

    # Converts the printed statements of the output to float and puts them in lists 
    while end_cond <= 1990:
        try:
            response = ser.readline().decode('utf-8').strip()
            values = response.split(',')
            
#             x_value = int(values[0])
#             y_value = float(values[1])
            
#             x_values.append(x_value)
#             y_values.append(y_value)
            
            end_cond += 10
        except ValueError:
            continue
    
    print(values)