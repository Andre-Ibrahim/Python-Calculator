def isFactorial(String):
    if(len(String) > 1 and String[len(String) - 1] == "!"):
        return True
    return False

def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)



def evali(x, y, op):
    if op == "+":
        return x + y
    if op == "-":
        return y - x
    if op == "*":
        return y * x
    if op == "^":
        return y ** x
    if op == "/":
        return y / x
    return 0

def evalb(y, x, op):
	if(op == ">"):
		return x > y
	if(op == "<"):
			return x < y
	if(op == "<="):
		return x <= y
	if(op == ">="):
		return x >= y
	if(op == "=="):
		return x == y
	if(op == "!="):
		return x != y
	return False
		
def isBoolean(x):
	if x == (">") or x == ("<") or \
    x == (">=") or x == ("<=") or x == ("==") or \
    x == ("!="):
		return True
	else:
		return False


def isDigit(x):
    try:
        int(x)
        return True
    except ValueError:
        return False

def priorityOP(x):
    
    if x == "!":
        return 2
    if x == "^":
        return 3
    if x == "*":
        return 4
    if x == "/":
        return 5
    if x == "+" or x == "-":
        return 6
    if x == "==" or x == "!=":
        return 7;
    return 8;

def claculate(statement):
    sarray = statement.split()
    if len(sarray) == 1:
        return sarray[0]
    
    for i, e in enumerate(sarray):
        if(isFactorial(e)):
            num = int(e[0, -1])
            num = str(factorial(num))
            sarray[i] = num
        
    maxIndex = 0
    priorityAtindex = 10
    operator = ""

    for i, e in enumerate(sarray):
        if i % 2 == 1 and priorityOP(sarray[i]) < priorityAtindex:
            maxIndex = i
            priorityAtindex = priorityOP(sarray[i])
            operator = sarray[i]
    if isBoolean(operator):
        temp = evalb(int(sarray[maxIndex + 1]), int(sarray[maxIndex - 1]), operator)
        return str(temp)
    else:
        x = evali(int(sarray[maxIndex + 1]), int(sarray[maxIndex - 1]), operator)
        sarray[maxIndex + 1] = None
        sarray[maxIndex - 1] = None
        sarray[maxIndex] = str(x)
    ret = ""

    for i, e in enumerate(sarray):
        if sarray[i] != None:
            ret += sarray[i] + " "
    return claculate(ret)
     
def compute(statement):
    if "(" not in statement:
        return claculate(statement)
    subCalculation = ""
    parenIndex = []

    for i, e in enumerate(statement):
        if statement[i] == "(":
            parenIndex.push(i)
        if statement[i] == ")":
            z = parenIndex.pop()
            subCalculation = claculate(statement[z + 1 : i])
            statement = statement[0:z] + subCalculation + statement[i + 1 : len(statement)]
            break
    return compute(statement)            


x = claculate("3 + 3 * 6 ^ 2")
print(x)