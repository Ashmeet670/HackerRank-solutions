import textwrap

def wrap(string, max_width):
    
    wrapper = textwrap.TextWrapper(width = max_width)
    listString = wrapper.wrap(string)
    newString = ""
    
    
    for i in listString:
        newString += i
        newString += "\n" 
        
    return(newString)
    
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)