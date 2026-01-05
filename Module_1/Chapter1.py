import math
def evaluate_f1_components(tp, fp, fn):
    if not isinstance(tp, int):
        print('tp must be int') 
        return
    if not isinstance(fp, int):
        print('fp must be int') 
        return
    if not isinstance(fn, int):
        print('fn must be int') 
        return    
    
    if tp < 0 or fp < 0 or fn < 0:
        print("tp and fp and fn must be greater or equal zero")
        return
    if (tp + fp) == 0 or (tp+fn) == 0:
        print("div for zero")
        return
          
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    if (precision + recall == 0):
        print('div for zero')
        return
    f1_score = 2 * ((precision * recall) / (precision + recall)) 
    
    print('precision is', precision)
    print('recall is', recall)
    print('f1_score is', f1_score)
    
    return precision, recall, f1_score 

       
# evaluate_f1_components(3,3,3)
# evaluate_f1_components(2,3,4)

def sigmoid(x):
    return 1 / (1 + (math.e)**(-x))

def reLU(x):
    if (x >=0):
        return x
    return 0

def ELU(x):
    a = 0.01
    if x <= 0:
        return a*((math.e)**x - 1)
    return x

def is_number(x):
    try:
        x = float(x)
        return True
    except ValueError:
        return False
    return True
    
def activation_function():
    x = input('input x: ')
    if not is_number(x):
        print("x must be a number")
        return
    x = float(x)
    act = input("Input activation Function (sigmoid|relu|elu):")
    if (act not in {"sigmoid","relu","elu"}):
        print(act, "is not supportted") 
        return
        
    if (act == 'sigmoid'):
        print("{}: f({}) = {}".format(act,x,sigmoid(x)))
    elif (act == 'relu'):
        print("{}: f({}) = {}".format(act,x,reLU(x)))
    else:
        print("{}: f({}) = {}".format(act,x,ELU(x)))
    
    
    
# print(reLU(-3))
# print(sigmoid(-3))
# print(ELU(-3))

activation_function()
    