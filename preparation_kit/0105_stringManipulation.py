


# Split: 'to this form' from combined form
# Combine: 'of this form' to combined form

# ***************************

# Method: methodName()
# Class: ClassName
# Variable: variableName

import sys
import re

for line in sys.stdin:
    operation = line.split(';')[0]
    method = line.split(';')[1]
    content = line.split(';')[2]
    
    if operation == 'S': # split the string
        stripedContent = content.rstrip() # strip of brackets
        stripedContent = stripedContent.strip('()')
        splitedText = re.split('(?<=.)(?=[A-Z])', stripedContent)
        lowerText = [x.lower() for x in splitedText] # make all lower
        finalText = ' '.join(lowerText) # join for final text
        print(finalText)
    elif operation == 'C': # combine the string
        stripedContent = content.strip() # strip of brackets
        splitedText = re.split(' ', stripedContent)
        # make all but first letter upper
        # combine
        if method == 'C': # create class name
            upperClass = [x[0].upper() + x[1:] for idx, x in enumerate(splitedText)] # first upper
            combinedClass = ''.join(upperClass)
            print(combinedClass)
        elif method == 'M': # create method name
            upperMethod = [x[0].upper() + x[1:] if idx > 0 else x for idx, x in enumerate(splitedText)] # first upper
            combinedMethod = ''.join(upperMethod)
            finalMethod = combinedMethod + '()'
            print(finalMethod)
        elif method == 'V': # create variable name
            upperVariable = [x[0].upper() + x[1:] if idx > 0 else x for idx, x in enumerate(splitedText)] # first upper
            finalVariable = ''.join(upperVariable)
            print(finalVariable)
        else:
            print('Second letter must be either M, V or C')
            break
    else:
        print('First letter must be either S or C')
        break