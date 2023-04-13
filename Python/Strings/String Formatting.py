def print_formatted(number):
    
    
    for i in range(1,number+1):
        decimal = str(i)
        octal = str(oct(i).replace("0o",""))
        hexa = str(hex(i).replace("0x","").upper())
        binary = str(bin(i).replace("0b",""))
        
        while len(decimal) != len(str(number)):
            decimal = " " + decimal
        
        while len(octal) != len(str(oct(number).replace("0o",""))):
            octal = " " + octal
        
        while len(hexa) != len(str(hex(number).replace("0x",""))):
            hexa = " " + hexa
        
        while len(binary) != len(str(bin(number).replace("0b",""))):
            binary = " " + binary
            
        totalSpace = len(binary)
        
        if len(decimal) != totalSpace:
            decimal = " "*(totalSpace - len(decimal)) + decimal
            
        if len(octal) != totalSpace:
            octal = " "*(totalSpace - len(octal)) + octal
            
        if len(hexa) != totalSpace:
            hexa = " "*(totalSpace - len(hexa)) + hexa
            
        
        
        print(f"{decimal} {octal} {hexa} {binary}")
    
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)