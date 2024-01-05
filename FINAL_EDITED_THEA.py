#Authors:
    # Gadil, Jea Anne
    # Leyco, Charlize Althea
    # Resuello, Roxanne Ysabel
    
import os
import re
from collections import OrderedDict
    
def readFile(file_name):
    # Get the current working directory
    current_directory = os.getcwd()
    
    # Create the full file path
    file_path = os.path.join(current_directory, file_name)
    
    contents = []
    try:
        # Check if the file exists
        if os.path.isfile(file_path):
            # Open the file in read mode
            with open(file_path, 'r') as file:
                # Read and print the contents
                #file_content = file.read()
                #print(f"File contents:\n{file_content}")
                for lines in file:
                    contents.append(lines.replace("\n", ""))
        else:
            print(f"Error: The file {file_name} does not exist in the current directory.")
    except Exception as e:
        print(f"An error occurred: {e}")
    # print("check here", contents)
    return contents

# Milestone 1 - lexical analyzer
#===========================================================

# Keywords dictionary
keywords = {
    "HAI" : "Code Delimiter"
    , "KTHXBYE" : "Code Delimiter"
    , "I HAS A" : "Variable Declaration"
    , "ITZ" : "Variable Assignment"
    , "R" : "Assignment Operator"
    , "SUM OF" : "Arithmetic Operator"
    , "DIFF OF" : "Arithmetic Operator"
    , "PRODUKT OF" : "Arithmetic Operator"
    , "QUOSHUNT OF" : "Arithmetic Operator"
    , "MOD OF" : "Arithmetic Operator"
    , "BIGGR OF" : "Arithmetic Operator"
    , "SMALLR OF" : "Arithmetic Operator"
    , "BOTH OF" : "Boolean Operator"
    , "EITHER OF" : "Boolean Operator"
    , "WON OF" : "Boolean Operator"
    , "NOT" : "Boolean Operator"
    , "ANY OF" : "Infinite Arity Operator"
    , "ALL OF" : "Infinite Arity Operator"
    , "MKAY" : "Infinite Arity Delimiter"
    , "BOTH SAEM" : "Comparison Operator"
    , "DIFFRINT" : "Comparison Operator"
    , "SMOOSH" : "Concatenation Operator"
    , "AN" : "Literal or Identifier Separator"
    , "MAEK" : "Typecast Operator"
    , "R MAEK": "Reassignment Operator"
    , "A" : "Typecast Separator"
    , "IS NOW A" : "Reassignment Operator"
    , "VISIBLE" : "Output Keyword"
    , "GIMMEH" : "Input Keyword"
    , "O RLY?" : "If Delimiter"
    , "YA RLY" : "If Keyword"
    , "MEBBE" : "Else-if Keyword"
    , "NO WAI" : "Else Keyword"
    , "OIC" : "If-Else or Switch-Case Delimiter"
    , "WTF?" : "Switch-Case Delimiter"
    , "OMG" : "Case Keyword"
    , "OMGWTF" : "Default Case Keyword"
    , "IM IN YR" : "Loop Start Delimiter"
    , "GTFO" : "Break Keyword"
    , "UPPIN" : "Increment Operator"
    , "NERFIN" : "Decrement Operator"
    , "YR" : "Loop Separator"
    , "TIL" : "FAIL Loop Repeater"
    , "WILE" : "WIN Loop Repeater"
    , "IM OUTTA YR" : "Loop End Delimiter"
    , "HOW IZ I" : "Function Delimiter"
    , "IF U SAY SO" : "Function Delimiter"
    # ADDED
    , "WAZZUP" : "Variable Keyword"
    , "BUHBYE" : "Variable Keyword"
    , "FOUND YR": "Return Keyword"
    , "I IZ": "Function Call keyword"
    , "+": "Printing Delimiter"
}

# Regex for identifier
identifier = "^[a-zA-Z][a-zA-Z0-9_]*$"

# Regex for NUMBR/NUMBAR (number) literals
literals = ["^-?\d+$", "^-?\d*\.\d+$"]

# Regex for YARN (string) literals
string_literal = "^\"[^”]*\"$"

# Regex for OIC, delimiter for if-else and switch-case
oic_pattern = r'^\s*OIC\s*$'

# Regex for TROOF (bool) literals
bool_literal = "(WIN|FAIL)"

# Regex for TYPE literals
type_literal = "(NOOB|TROOF|NUMBAR|NUMBR|YARN)"
type_literal_syntax = ["NOOB", "TROOF", "NUMBAR", "NUMBR", "YARN"]

# Additional regex for the semantics analyzer 
wazzup_pattern = re.compile(r'^WAZZUP$')
buhbye_pattern = re.compile(r'^BUHBYE$')
kthxbye_pattern = re.compile(r'^KTHXBYE$')
# smoosh_pattern = re.compile(r'SMOOSH\s+"?[\w.]+"?(?:\s+AN\s+"?[\w.]+"?)*\s*$')
# check this
smoosh_pattern = re.compile(r'^SMOOSH\s+(\S+(\s+AN\s+(\S+|"([^"]*)"))*)\s*$')
smoosh_pattern_forfunc = r'SMOOSH\s+(\S+(\s+AN\s+(\S+|"([^"]*)"))*)\s*'
arithmetic_pattern = r'(SUM OF|DIFF OF|PRODUKT OF|QUOSHUNT OF|MOD OF|BIGGR OF|SMALLR OF|BOTH OF|EITHER OF|WON OF|BOTH SAEM|DIFFRINT) ([a-zA-Z][a-zA-Z0-9_]*|[0-9]*\.?[0-9]+) (AN) ([a-zA-Z][a-zA-Z0-9_]*|[0-9]*\.?[0-9]+)'
boolean_operation = r'(NOT|BOTH OF|EITHER OF|WON OF) ([a-zA-Z][a-zA-Z0-9_]*|[0-9]*\.?[0-9]+) (AN [a-zA-Z][a-zA-Z0-9_]*|[0-9]*\.?[0-9]+)'
# literal_pattern = r'([0-9]+|[0-9]+\.[0-9]+|".*"|WIN|FAIL)'
literal_pattern = r'([0-9]+|[0-9]+\.[0-9]+|"[^"]*"|WIN|FAIL)'
comparison_pattern = r'(BOTH SAEM|DIFFRINT) (.+?) AN (.+)'

variable_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'
variable_pattern_forfunc = r'[a-zA-Z_][a-zA-Z0-9_]*'
integer_pattern = r'^[+-]?\d+$'
float_pattern = r'^[+-]?\d+(\.\d+)?$'
boolean_pattern = r'^(WIN|FAIL)$'
yarn_pattern = r'".*"'
variable_declaration_pattern = re.compile(r'^I HAS A ([a-zA-Z]+[a-zA-Z0-9_]*)( ITZ (' + arithmetic_pattern + '|' + literal_pattern + '|' + variable_pattern + '|' + comparison_pattern + '|' + boolean_operation + '))?\s*( BTW .*)?$') 
typecast_pattern = re.compile(r'^MAEK ([a-zA-Z]+[a-zA-Z0-9_]*)( A (' + '|'.join(type_literal_syntax[:-1]) + ')| ' + type_literal_syntax[-1] + ')\s*( BTW .*)?\s*$')
reassignment_pattern = re.compile(r'^([a-zA-Z]+[a-zA-Z0-9_]*)\s*((IS NOW A)\s*(' + '|'.join(type_literal_syntax) + ')|(R MAEK)\s*([a-zA-Z]+[a-zA-Z0-9_]*)\s*(' + '|'.join(type_literal_syntax) + '))\s*(BTW .*)?$')       
assignment_pattern = re.compile(r'^([a-zA-Z]+[a-zA-Z0-9_]*)( R (' + arithmetic_pattern + '|' + literal_pattern + '|' + variable_pattern + '|' + comparison_pattern + '|' + boolean_operation + '))?\s*( BTW .*)?$')        
loop_pattern = re.compile(r"IM IN YR ([a-zA-Z][a-zA-Z0-9_]*) (UPPIN|NERFIN) YR ([a-zA-Z][a-zA-Z0-9_]*) ((TIL|WILE) (.+))?")
function_pattern = re.compile(r'HOW IZ I (\w+)(?: YR (\w+)(?: AN YR (\w+)(?: AN YR (\w+))?)?)? *$')
# function_pattern = re.compile(r'HOW IZ I (\w+)(?: YR ([a-zA-Z_][a-zA-Z0-9_]*)(?: AN YR ([a-zA-Z_][a-zA-Z0-9_]*)(?: AN YR ([a-zA-Z_][a-zA-Z0-9_]*))?)?)? *$')
# variable_function_pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')

# Potential keywords array
potential_keyword = ["I", "I HAS", "SUM", "DIFF", "PRODUKT", "QUOSHUNT", "MOD"
                    , "BIGGR", "SMALLR", "BOTH", "EITHER", "WON", "ANY", "ALL"
                    , "IS", "IS NOW", "O", "YA", "NO", "IM", "IM IN", "IM OUTTA"
                    , "HOW", "HOW IZ", "IF", "IF U", "IF U SAY", "FOUND"]

# To remove comment in the line and tuples
to_remove = {'Multi-Line Comment', 'Single Line Comment', 'Single Line Comment Declaration', 'Multi-Line Comment Declaration'}

# flags
obtw = False
wazzup = False
hai = False
multi_line = False
obtw_line = 0
comments = False
comments_next = False
inside_wazzup_buhbye = False
if_delimiter = False
oic_found = False
if_keyword = False
else_keyword = False
wazzup_line = 0
variables = {}
functions = {}
if_else_condition = []
condition_index = []
loop_lines = []
loop_tokens = []
is_loop = False
is_var_assignment = False

#for function
function_lines =  []
function_tokens = []
is_function = False

#for switch case
switch_delimiter = False
switch_case_condition = []
temp = 0
default_case_index = 0
case_keyword = False
default_case_keyword = False

datatypes = {
    'int': "NUMBR",
    'float' : "NUMBAR",
    'str' : "YARN",
    'bool' : "TROOF",
    'NoneType' : "NOOB"
}

def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def error_prompt(line_number, error_message):
    print(f"Error in line {line_number}: {error_message}")
    exit(0)

def arithmetic(line_number, stack, operation):
    operations_dict = {
        "SUM OF": "+",
        "DIFF OF": "-",
        "PRODUKT OF": "*",
        "QUOSHUNT OF": "/",
        "MOD OF": "%",
        "BIGGR OF": "max",
        "SMALLR OF": "min",
    }
    if len(stack) < 2:
        error_prompt(line_number, "Arithmetic expression error.")
    
    op2 = stack.pop()
    op1 = stack.pop()

    # if op2 is True or False, convert to 1 or 0
    if op2 == True:
        op2 = 1
    elif op2 == False:
        op2 = 0

    # if op1 is True or False, convert to 1 or 0
    if op1 == True:
        op1 = 1
    elif op1 == False:
        op1 = 0
    try:
        if operations_dict[operation] == "max":
            result = max(op2, op1)
        elif operations_dict[operation] == "min":
            result = min(op2, op1)
        else:
            result = eval(f"{op2} {operations_dict[operation]} {op1}")

            # Check if the operation is division
            if operations_dict[operation] == "/":
                # Check if the operands are integers
                if isinstance(op1, int) and isinstance(op2, int):
                    result = int(result)
    except:
        error_prompt(line_number, "Arithmetic expression error.")

    stack.append(result)
    return stack

def boolean(line_number, stack, operation):
    operations_dict = {
        "BOTH OF": "and",
        "EITHER OF": "or",
        "WON OF": "^",
        "NOT": "!",
    }

    if len(stack) < 2 and operation != "NOT":
        error_prompt(line_number, "Boolean expression error.")

    if operation == "NOT":
        try:
            op1 = stack.pop()
            result = not op1
            stack.append(result)
            return stack
        except:
            error_prompt(line_number, "Boolean expression error.")
    else:
        op2 = stack.pop()
        op1 = stack.pop()

        # if op2 is True or False, convert to 1 or 0
        if float(op2) == 1.0:
            op2 = True
        elif op2 == 0:
            op2 = False

        # if op1 is True or False, convert to 1 or 0
        if float(op1) == 1.0:
            op1 = True
        elif op1 == 0:
            op1 = False

        try:
            result = eval(f"{op2} {operations_dict[operation]} {op1}")
        except:
            error_prompt(line_number, "Boolean expression error.")
    
    stack.append(result)
    return stack

def comparison(line_number, stack, operation):
    operations_dict = {
        "BOTH SAEM": "==",
        "DIFFRINT": "!=",
    }

    try:
        if len(stack) < 2:
            error_prompt(line_number, "Comparison expression error.")

        op2 = stack.pop()
        op1 = stack.pop()

        result = eval(f"{op2} {operations_dict[operation]} {op1}")
    except:
        error_prompt(line_number, "Comparison expression error.")

    stack.append(result)
    return stack

def arithmetic_analyzer(line, line_number, untokenized_line):
    global inside_wazzup_buhbye, wazzup_line, if_keyword, else_keyword, case_keyword, default_case_keyword

    

    if if_keyword == True and if_delimiter == False:
        if_keyword = False
        return

    if else_keyword == True and if_delimiter == False:
        else_keyword = False
        return
    
    if case_keyword == True and switch_delimiter == False:
        case_keyword = False
        return

    if default_case_keyword == True and switch_delimiter == False:
        default_case_keyword = False
        return
    
    # this is to ensure that the wazzup and buhbye block only contains variable declaration 
    # also, this checks whether the wazzup has corresponding buhbye, and vice versa
    if inside_wazzup_buhbye == True:
        match = variable_declaration_pattern.match(untokenized_line)
        match_code_delim = kthxbye_pattern.match(untokenized_line)
        if 'BUHBYE' in untokenized_line:
            if inside_wazzup_buhbye == False:
                print(f"Error in line {line_number}: No matching WAZZUP declaration.")
                exit(0)
            if not buhbye_pattern.match(untokenized_line):
                print(f"Error in line {line_number}: BUHBYE should be alone on its line.")
                exit(0)
            else:
                wazzup_line -=1
                inside_wazzup_buhbye = False
        elif match_code_delim:
            if wazzup_line != 0:
                print(f"Error in line {line_number}: No matching BUHBYE declaration.")
                exit(0)
        elif not match:
            print(f"Error in line {line_number}: Must be variable declaration only.")
            # pass
            exit(0)


    prev = ""
    stack = []
    isInfiniteAnd = False
    isInfiniteOr = False

    # Check if infinite arity operator is present
    if line[0][0] == "ALL OF":
        if line[-1][0] == "MKAY":
            isInfiniteAnd = True
        else:
            error_prompt(line_number, "Boolean expression error.")
    elif line[0][0] == "ANY OF":
        if line[-1][0] == "MKAY":
            isInfiniteOr = True
        else:   
            error_prompt(line_number, "Boolean expression error.")

    revline = line[::-1] 

    counter = 0
    for word in revline:
        # print(f"word: {word} - prev: {prev}")

        counter += 1
        # ======================== CHECK SYNTAX
        if counter == 1:
            if word[1] == "String Literal" or word[1] == "NUMBR Literal" or word[1] == "NUMBAR Literal" or word[1] == "TROOF Literal" or word[1] == "Identifier":
                prev = "operand"
        else:
            if counter != len(revline) and (isInfiniteAnd == True or isInfiniteOr == True):
                if word[0] == "ALL OF" or word[0] == "ANY OF":
                    error_prompt(line_number, "Expression error.")

            if prev == "operand":
                if word[1] == "Arithmetic Operator" or word[1] == "Boolean Operator" or word[1] == "Comparison Operator":
                    prev = "operator"
                elif word[0] == "AN":
                    prev = "AN"
                else:
                    error_prompt(line_number, "Expression error.")
            elif prev == "operator":
                if word[1] == "Arithmetic Operator" or word[1] == "Boolean Operator":
                    prev = "operator"
                elif word[0] == "AN":
                    prev = "AN"
                else:
                    error_prompt(line_number, "Arithmetic expression error.")
            elif prev == "AN" :
                if word[0] == "AN" or word[1] == "Arithmetic Operator" or word[1] == "Boolean Operator" or word[1] == "Comparison Operator":
                    error_prompt(line_number, "Expression error.")
                else:
                    prev = "operand"


        # ======================== EVALUATE SEMANTICS
        # AFTER CHECKING IF THE CURRENT WORD HAS CORRECT TYPE, UPDATE PREV

        # IF OPERATION, PERFORM
        if word[1] == "Arithmetic Operator":
            # print(stack)
            # if current token is an arithmetic operator
            stack = arithmetic(line_number, stack, word[0])
            # print(stack)
        elif word[1] == "Boolean Operator":
            stack = boolean(line_number, stack, word[0])
        elif word[1] == "Comparison Operator":
            stack = comparison(line_number, stack, word[0])
        
        # IF OPERAND, ADD TO STACK
        elif word[0] in variables:
            operand = stack.append(variables[word[0]]['value'])
            if variables[word[0]]['data type'] == 'NUMBR Literal' or variables[word[0]]['data type'] == 'NUMBAR Literal' or variables[word[0]]['data type'] == 'TROOF Literal':
                if variables[word[0]]['data type'] == 'TROOF Literal':
                    if variables[word[0]]['value'] == 'WIN':
                        stack.append(True)
                    else:
                        stack.append(False)
                else:
                    stack.append(variables[word[0]]['value'])
        else:
            #print(f'num: {word[0]}')
            # Check if the element is a string and if it's a float or int

            
            try:
                # Check if the element is enclosed in quotation marks
                if word[0].startswith('"') and word[0].endswith('"'):
                    # Attempt to extract the number inside the quotes
                    num = word[0][1:-1]
                    # Check if the num is an integer or float
                    if is_integer(num):
                        stack.append(int(num))
                    elif is_float(num):
                        stack.append(float(num))
                else:
                    # Check if the element is a string and if it's a float or int
                    # Check if the num is an integer or float
                    num = word[0]
                    if is_integer(num):
                        stack.append(int(num))
                    elif is_float(num):
                        stack.append(float(num))

                if word[0] == "WIN":
                    stack.append(True)
                elif word[0] == "FAIL":
                    stack.append(False)
            except ValueError:
                error_prompt(line_number, "Arithmetic expression error.")

        # If last element in revline and len(stack) != 1, print error
                
        if counter == len(revline) and len(stack) != 1 and isInfiniteAnd == False and isInfiniteOr == False:
            print(f"Error in line {line_number}: Arithmetic expression error.")
            return
        elif isInfiniteAnd == True:
            try:
                result = all(stack)
            except:
                error_prompt(line_number, "Boolean expression error.")
            return result
        elif isInfiniteOr == True:
            try:
                result = any(stack)
            except:
                error_prompt(line_number, "Boolean expression error.")
            return result
    
    #print(stack)
    if len(stack) != 1:
        error_prompt(line_number, "Expression error.")

    global is_var_assignment

    if is_var_assignment == False:
        if stack[0] is not None:
            if stack[0] == True:
                variables['IT'] = {'value': "WIN", 'data type': "TROOF"}
            elif stack[0] == False:
                variables['IT'] = {'value': "FAIL", 'data type': "TROOF"}
            else:
                variables['IT'] = {'value': stack[0], 'data type': datatypes[type(stack[0]).__name__]}
    else:
        is_var_assignment = False
    
    if stack[0] == True:
        return "WIN"
    elif stack[0] == False:
        return "FAIL"
    else:
        return stack[0]

def print_analyzer(line, line_number):
    global is_var_assignment
    isStart = True
    hasOperand = True
    global inside_wazzup_buhbye, wazzup_line
    toprint = ""

    if if_keyword == True and if_delimiter == False:
        return

    if else_keyword == True and if_delimiter == False:
        return
    
    # this is to ensure that the wazzup and buhbye block only contains variable declaration 
    # also, this checks whether the wazzup has corresponding buhbye, and vice versa
    if inside_wazzup_buhbye == True:
        match = variable_declaration_pattern.match(line)
        match_code_delim = kthxbye_pattern.match(line)
        if 'BUHBYE' in line:
            if inside_wazzup_buhbye == False:
                print(f"Error in line {line_number}: No matching WAZZUP declaration.")
                exit(0)
            if not buhbye_pattern.match(line):
                print(f"Error in line {line_number}: BUHBYE should be alone on its line.")
                exit(0)
            else:
                wazzup_line -=1
                inside_wazzup_buhbye = False
        elif match_code_delim:
            if wazzup_line != 0:
                print(f"Error in line {line_number}: No matching BUHBYE declaration.")
                exit(0)
        elif not match:
            print(f"Error in line {line_number}: Must be variable declaration only.")
            # pass
            exit(0)

    operands = []
    

    operand = []
    #print(line)
    counter = 0
    
    for word in line:

        counter += 1
        #print(f"word: {word}")
        if word[0] == "VISIBLE" and isStart == True:  # Correct the condition here
            isStart = False
        elif word[1] == "Printing Delimiter" or counter == len(line):
            #print(f"word: {word}")
            #print(f"OPERANDDDD")
            if counter == len(line):
                operand.append(word)
                operands.append(operand.copy())  # Use copy to avoid modifying the original list
                operand.clear()
            else:
                operands.append(operand.copy())  # Use copy to avoid modifying the original list
                operand.clear()
        else:
           # print("HERE")
            operand.append(word)
    #print(f"OPERANDS: {operands}")

    for op in operands:
        #print(f"OPERAND: {operand}")
        if len(op) == 1:
            if op[0][1] == "String Literal":
                toprint += op[0][0][1:-1]
            elif op[0][1] == "NUMBR Literal" or op[0][1] == "NUMBAR Literal" or op[0][1] == "TROOF Literal":
                toprint += op[0][0]
            elif op[0][1] == "Identifier":
                try:
                    toprint += str(variables[op[0][0]]['value'])
                except:
                    error_prompt(line_number, f"Variable {op[0][0]} is not yet declared.")
            else:
                error_prompt(line_number, "Print expression error.")
        else:
            expression = ""
            for word in op:
                expression += word[0]
                expression += " "
            
            if op[0][1] == "Arithmetic Operator" or op[0][1] == "Boolean Operator" or op[0][1] == "Comparison Operator":
                #print(f"expression: {expression[:-1]}")
                new_value = arithmetic_analyzer(op, line_number, expression[:-1])
                toprint += str(new_value)
            else:
                try:
                    new_value = analyze(op, line_number, expression[:-1])
                    toprint += str(new_value)
                except:
                    error_prompt(line_number, "Print expression error.")

    return toprint

def input_analyzer(line, line_number, untokenized_line):
    print(line)
    print(untokenized_line)
    if len(line) != 2:
        error_prompt(line_number, "Input expression error.")
    else:
        if line[1][1] == "Identifier":
            try:
                user_input = input()
                variables[line[1][0]]['value'] = str(user_input)
                variables[line[1][0]]['data type'] = 'YARN'
            except:
                error_prompt(line_number, "Input expression error.")
        else:
            error_prompt(line_number, "Input expression error.")

def remove_comments(line, all_tokens):
    global to_remove
    words_to_remove = []
    
    for token in all_tokens[1:]:
        word, classification = token
        if classification in to_remove:
            words_to_remove.append(word)
    
    if len(words_to_remove) == 0:
        return line
    else:
        for remove in words_to_remove:
            line = line.replace(remove, '')
        return line

#This function checks for single line and multi-line comment errors
#if an error exists, prints the appropriate error message, else returns bool comment_error
def check_comment_errors(line, line_number):
    global obtw, obtw_line, comments

    comment_error = False
    
    if re.search(r'OBTW', line):
        # print(line)
        #set flags to true
        obtw = True
        obtw_line = line_number
        if re.compile(r'^(?!OBTW).+').match(line):
            print(f"Error in line {line_number}: Multi-line commment error.")
            comment_error = True
            exit(0)
            
    if re.search(r'TLDR', line): 
        # no OBTW 
        if not obtw:
            print(f"Error in line {line_number}: No matching multi-line commment declaration.")
            comment_error = True
            exit(0)
        if line != "TLDR":
            print(f"Error in line {line_number}: Multi-line commment delimiter error.")
            comment_error = True
            exit(0)
        obtw = False
    
    return comment_error

expression = {"Variable Declaration", "Variable Assignment", "Identifier"}

def get_data_type(variable_to_analyze):
    data_type = ""
    if re.match(r'\d+\.\d+', variable_to_analyze): 
        data_type = "NUMBAR"
    elif variable_to_analyze.isdigit():  
        data_type = "NUMBR"
    elif variable_to_analyze in ('WIN', 'FAIL'):  
        data_type = "TROOF"
    elif variable_to_analyze.startswith('"') and variable_to_analyze.endswith('"'): 
        data_type = "YARN"
    elif variable_to_analyze == "None":
        data_type = "NOOB"
    else:
        data_type = "ELSE"
        
    return data_type

#This function checks the syntax 
def analyze(line, classification, line_number, all_tokens):

    global obtw, obtw_line, comments, inside_wazzup_buhbye, wazzup_line, expression, if_keyword, variables
    global else_keyword, case_keyword, default_case_keyword
    
    if if_keyword == True and if_delimiter == False:
        if_keyword = False
        return

    if else_keyword == True and if_delimiter == False:
        else_keyword = False
        return
    
    if case_keyword == True and switch_delimiter == False:
        case_keyword = False
        return

    if default_case_keyword == True and switch_delimiter == False:
        default_case_keyword = False
        return
    
    # this is to ensure that the wazzup and buhbye block only contains variable declaration 
    # also, this checks whether the wazzup has corresponding buhbye, and vice versa
    if inside_wazzup_buhbye == True:
        match = variable_declaration_pattern.match(line)
        match_code_delim = kthxbye_pattern.match(line)
        if 'BUHBYE' in line:
            if inside_wazzup_buhbye == False:
                print(f"Error in line {line_number}: No matching WAZZUP declaration.")
                exit(0)
            if not buhbye_pattern.match(line):
                print(f"Error in line {line_number}: BUHBYE should be alone on its line.")
                exit(0)
            else:
                wazzup_line -=1
                inside_wazzup_buhbye = False
        elif match_code_delim:
            if wazzup_line != 0:
                print(f"Error in line {line_number}: No matching BUHBYE declaration.")
                exit(0)
        elif not match:
            print(f"Error in line {line_number}: Must be variable declaration only.")
            exit(0)
        
# ======================================INPUT================================
    if re.match(r'^\s*GIMMEH', line):
        # Check if the syntax is correct
        input_match = re.match(r'^\s*GIMMEH\s+([a-zA-Z][a-zA-Z0-9_]*)\s*(?:BTW .*)?$', line)
        if input_match:
            input_analyzer(all_tokens, line_number, line)
        else:
            print(f"Error in line {line_number}: Incorrect format for input.")
            exit(0)
            
# ======================================CONCATENATION======================================
    #check for concatenation
    if re.match(r'^\s*SMOOSH', line):
        # Check if the syntax is correct
        smoosh_match = re.match(smoosh_pattern, line)
        if smoosh_match:            
            #Get all tokens
            tokens = smoosh_match.group(1).split(' AN ')
            
            # print("tokenstokenstokens", tokens)
            correct_values = True

            to_concat = []

            for token in tokens:
                token_data_type = get_data_type(token)
                
                if token_data_type in ("NUMBAR", "NUMBR", "TROOF", "YARN"): 
                    to_concat.append(token)
                else: 
                #check if the variables are declared
                    if token in variables:
                        var_value = str(variables[token]['value'])
                        to_concat.append(var_value)
                    else:
                        print(f"Error in line {line_number}: Variable '{token}' is not yet declared.")
                        correct_values = False
                        exit(0)

            # for token in tokens:
            #     if token[0]:  # Check if the first capturing group is not empty (string within double quotes)
            #         string_value = token[0]
            #         to_concat.append(string_value)
            #     else:
            #         value = token[1]
            #         if value in {'WIN', 'FAIL'}:
            #             to_concat.append(value)
            #         else:
            #             try:
            #                 number_value = int(value)
            #                 to_concat.append(number_value)
            #             except ValueError:
            #                 try:
            #                     float_value = float(value)
            #                     to_concat.append(float_value)
            #                 except ValueError:
            #                     # other_list.append(value)
            #                     #check if the variables are declared
            #                     if value in variables:
            #                         var_value = str(variables[value]['value'])
            #                         to_concat.append(var_value)
            #                     else:
            #                         print(f"Error in line {line_number}: Variable '{value}' is not yet declared.")
            #                         correct_values = False
            #                         exit(0)
                                    
            if correct_values == True:
                concatenated = ''.join([str(s).strip('"') for s in to_concat])
                concatenated = "\"" + concatenated + "\""
                print("Resulting string after concatenationnnnnn:", concatenated)
                if 'IT' not in variables:
                    variables['IT'] = {'value': concatenated, 'data type': 'YARN'}
                else:
                    variables['IT']['value'] = concatenated
                    variables['IT']['data type'] = 'YARN'
                return concatenated
        else: 
            # errors.append(f"Error in line {line_number}: Incorrect format for concatenation.")
            print(f"Error in line {line_number}: Incorrect format for concatenation.")
            exit(0)
    
    #check for variable declaration
    if 'WAZZUP' in line:
        
        if not wazzup_pattern.match(line):
            print(f"Error in line {line_number}: WAZZUP should be alone on its line.")
            exit(0)
        else:
            inside_wazzup_buhbye = True
            wazzup_line += 1

    if classification == "Variable Declaration":
        if inside_wazzup_buhbye == True:
            match = variable_declaration_pattern.match(line)
            if match:
                variable_name = match.group(1)
                initial_value = match.group(3)
                if initial_value in variables:
                    temp_val = variables[initial_value]['value']
                    temp_type = variables[initial_value]['data type']
                    variables[variable_name] = {'value': temp_val, 'data type': temp_type}
                else:
                    if initial_value is not None:
                        if re.match(integer_pattern, initial_value):
                            variables[variable_name] = {'value': int(initial_value.strip()), 'data type': 'NUMBR'}
                        elif re.match(float_pattern, initial_value):
                            variables[variable_name] = {'value': float(initial_value.strip()), 'data type': 'NUMBAR'}
                        elif re.match(boolean_pattern, initial_value):
                            variables[variable_name] = {'value': initial_value.strip(), 'data type': 'TROOF'}
                        elif re.match(arithmetic_pattern, initial_value) or re.match(boolean_operation, initial_value) or re.match(comparison_pattern, initial_value):
                                # print("DETECTED")
                                global is_var_assignment
                                is_var_assignment = True
                                filtered_tokens = [(value, category) for value, category in all_tokens if category not in expression]
                                new_value = arithmetic_analyzer(filtered_tokens, line_number, line)
                                # print("new value", new_value)
                                if re.match(integer_pattern, str(new_value)):
                                    variables[variable_name] = {'value': int(new_value), 'data type': 'NUMBR'}
                                elif re.match(float_pattern, str(new_value)):
                                    variables[variable_name] = {'value': float(new_value), 'data type': 'NUMBAR'}
                                elif re.match(boolean_pattern, str(new_value)):
                                    variables[variable_name] = {'value': str(new_value), 'data type': 'TROOF'}
                                
                        elif re.match(yarn_pattern, initial_value):
                                variables[variable_name] = {'value': initial_value.strip(), 'data type': 'YARN'}
                        else:
                            print(f"Error in line {line_number}: Variable declaration error.")
                            exit(0)
                    else:
                        variables[variable_name] = {'value': None, 'data type': 'NOOB'}
                    
                    
            else:
                # errormess = f"Error in line {line_number}: Variable declaration error."
                print(f"Error in line {line_number}: Variable declaration error.")
                exit(0)
        else:
            
            print(f"Error in line {line_number}: Variable declaration error. Must be inside WAZZUP BUHBYE block.")
            exit(0)

    elif classification == "Typecast Operator":
        # MAEK operator only modifies the resulting value
        # thus, the typecasting here is stored in the key 'IT'
        match = typecast_pattern.match(line)
        if match:
            variable_name = match.group(1)
            variable_type = match.group(3) if match.group(3) else match.group(2)
            print(variable_name, variable_type)

            # print("dito ulit", variable_type)
            if variable_name in variables:
                if 'IT' not in variables:
                    variables['IT'] = {'value': None, 'data type': 'NOOB'} 
                else:
                    if variable_type == 'NUMBR':
                        if variables[variable_name]['data type'] == 'NUMBAR':
                            variables['IT']['value'] = int(variables[variable_name]['value'])
                            variables['IT']['data type'] = 'NUMBR'
                        elif variables[variable_name]['data type'] == 'TROOF':
                            if variables[variable_name]['value'] == 'WIN':
                                variables['IT']['value'] = 1
                                variables['IT']['data type'] = 'NUMBR'
                            else:
                                variables['IT']['value'] = 0
                                variables['IT']['data type'] = 'NUMBR'
                        elif variables[variable_name]['data type'] == 'YARN':
                            var_value = variables[variable_name]['value']
                            var_strip = var_value.strip('\"')
                            # print("STOPPPP",variables[variable_name]['value'].isnumeric())
                            if var_strip.isnumeric():
                                variables['IT']['value'] = int(var_strip)
                                variables['IT']['data type'] = 'NUMBR'
                            else:
                                print(f"Error in line {line_number}: Cannot cast non-numeric YARN to NUMBR.")
                        elif variables[variable_name]['data type'] == 'NOOB':
                            variables['IT']['value'] = 0
                            variables['IT']['data type'] = 'NUMBR'
                        

                    elif variable_type == 'NUMBAR':
                        if variables[variable_name]['data type'] == 'NUMBR':
                            variables['IT']['value'] = float(variables[variable_name]['value'])
                            variables['IT']['data type'] = 'NUMBAR'
                        elif variables[variable_name]['data type'] == 'TROOF':
                            if variables[variable_name]['value'] == 'WIN':
                                variables['IT']['value'] = 1.0
                                variables['IT']['data type'] = 'NUMBAR'
                            else:
                                variables['IT']['value'] = float(0)
                                variables['IT']['data type'] = 'NUMBAR'
                        elif variables[variable_name]['data type'] == 'YARN':
                            var_value = variables[variable_name]['value']
                            var_strip = var_value.strip('\"')
                            # print("STOPPPP",variables[variable_name]['value'].isnumeric())
                            if var_strip.isnumeric():
                                variables['IT']['value'] = int(var_strip)
                                variables['IT']['data type'] = 'NUMBAR'
                            else:
                                print(f"Error in line {line_number}: Cannot cast non-numeric YARN to NUMBAR.")
                                exit(0)
                        elif variables[variable_name]['data type'] == 'NOOB':
                            variables['IT']['value'] = float(0)
                            variables['IT']['data type'] = 'NUMBAR'

                    elif variable_type == 'YARN':
                        if variables[variable_name]['data type'] == 'NUMBAR':
                            formatted_value = "{:.2f}".format(variables[variable_name]['value'])
                            variables['IT']['value'] = formatted_value
                            variables['IT']['data type'] = 'YARN'
                        elif variables[variable_name]['data type'] == 'NUMBR':
                            variables['IT']['value'] = str(variables[variable_name]['value'])
                            variables['IT']['data type'] = 'YARN'
                        elif variables[variable_name]['data type'] == 'NOOB':
                            variables['IT']['value'] = ""
                            variables['IT']['data type'] = 'YARN'
                    
                    elif variable_type == 'TROOF':
                        if variables[variable_name]['data type'] == 'NOOB' or variables[variable_name]['value'] == None or variables[variable_name]['value'] == 0 or variables[variable_name]['value'] == float(0) or variables[variable_name]['value'] == "":
                            variables['IT']['value'] = 'FAIL'
                            variables['IT']['data type'] = 'TROOF'
                        else:
                            variables['IT']['value'] = 'WIN'
                            variables['IT']['data type'] = 'TROOF'
                        
                    else:
                        print(variable_type)
                        print(f"Error in line {line_number}: Typecast error.")
                        exit(0)

            else:
                print(f"Error in line {line_number}: Variable does not exist.")
                exit(0)
                
        else:
            print(f"Error in line {line_number}: ssTypecast error.")
            exit(0)
    
    elif classification == "Reassignment Operator":
        #make a regex for reassignment operator for lolcode 
        match = reassignment_pattern.match(line)
        if match:
            variable_name = match.group(1)
            if match.group(3) == 'IS NOW A':
                variable_type = match.group(4)
            else: # 'R MAEK'
                variable_type = match.group(7)
            # print(variable_name, variable_type)
            if variable_name in variables:
                if variable_type == 'NUMBR':
                    if variables[variable_name]['data type'] == 'NUMBAR':
                        variables[variable_name]['value'] = int(variables[variable_name]['value'])
                        variables[variable_name]['data type'] = 'NUMBR'
                    elif variables[variable_name]['data type'] == 'TROOF':
                        if variables[variable_name]['value'] == 'WIN':
                            variables[variable_name]['value'] = 1
                            variables[variable_name]['data type'] = 'NUMBR'
                        else:
                            variables[variable_name]['value'] = 0
                            variables[variable_name]['data type'] = 'NUMBR'
                    elif variables[variable_name]['data type'] == 'YARN':
                        if variables[variable_name]['value'].isnumeric():
                            variables[variable_name]['value'] = int(variables[variable_name]['value'])
                            variables[variable_name]['data type'] = 'NUMBR'
                        else:
                            print(f"Error in line {line_number}: Cannot reassign non-numeric YARN to NUMBR.")
                            exit(0)
                    elif variables[variable_name]['data type'] == 'NOOB':
                        variables[variable_name]['value'] = 0
                        variables[variable_name]['data type'] = 'NUMBR'
                    

                elif variable_type == 'NUMBAR':
                    if variables[variable_name]['data type'] == 'NUMBR':
                        variables[variable_name]['value'] = float(variables[variable_name]['value'])
                        variables[variable_name]['data type'] = 'NUMBAR'
                    elif variables[variable_name]['data type'] == 'TROOF':
                        if variables[variable_name]['value'] == 'WIN':
                            variables[variable_name]['value'] = 1.0
                            variables[variable_name]['data type'] = 'NUMBAR'
                        else:
                            variables[variable_name]['value'] = float(0)
                            variables[variable_name]['data type'] = 'NUMBAR'
                    elif variables[variable_name]['data type'] == 'YARN':
                        if variables[variable_name]['value'].isnumeric():
                            variables[variable_name]['value'] = float(variables[variable_name]['value'])
                            variables[variable_name]['data type'] = 'NUMBAR'
                        else:
                            print(f"Error in line {line_number}: Cannot reassign non-numeric YARN to NUMBAR.")
                            exit(0)
                    elif variables[variable_name]['data type'] == 'NOOB':
                        variables[variable_name]['value'] = float(0)
                        variables[variable_name]['data type'] = 'NUMBAR'
                
                elif variable_type == 'YARN':
                    if variables[variable_name]['data type'] == 'NUMBAR':
                        formatted_value = "{:.2f}".format(variables[variable_name]['value'])
                        variables[variable_name]['value'] = formatted_value
                        variables[variable_name]['data type'] = 'YARN'
                    elif variables[variable_name]['data type'] == 'NUMBR':
                        variables[variable_name]['value'] = str(variables[variable_name]['value'])
                        variables[variable_name]['data type'] = 'YARN'
                    elif variables[variable_name]['data type'] == 'NOOB':
                        variables[variable_name]['value'] = ""
                        variables[variable_name]['data type'] = 'YARN'
                
                elif variable_type == 'TROOF':
                    if variables[variable_name]['data type'] == 'NOOB' or variables[variable_name]['value'] == None or variables[variable_name]['value'] == 0 or variables[variable_name]['value'] == float(0) or variables[variable_name]['value'] == "":
                        variables[variable_name]['value'] = 'FAIL'
                        variables[variable_name]['data type'] = 'TROOF'
                    else:
                        variables[variable_name]['value'] = 'WIN'
                        variables[variable_name]['data type'] = 'TROOF'
                
                else:
                    print(f"Error in line {line_number}: Reassignment error.")
                    exit(0)
        else:
            print(f"Error in line {line_number}: Reassignment error.")
            exit(0)

    elif classification == "Assignment Operator":
        #make a regex for assignment operator for lolcode 
        # print("d2 ba")
        match = assignment_pattern.match(line)
        if match:
            # print("yes")
            variable_name = match.group(1)
            # print("dito be", variable_name)
            variable_val = match.group(3)
            # print(variable_name, variable_val)
            if variable_name in variables:
                if variable_val in variables:
                    temp_val = variables[variable_val]['value']
                    temp_type = variables[variable_val]['data type']
                    variables[variable_name]['value'] = temp_val
                    variables[variable_name]['data type'] = temp_type
                else:
                    if re.match(integer_pattern, variable_val):
                        # variables[variable_name] = {'value': int(initial_value.strip()), 'data type': 'NUMBR'}
                        variables[variable_name]['value'] = int(variable_val)
                        variables[variable_name]['data type'] = 'NUMBR'
                    elif re.match(float_pattern, variable_val):
                        variables[variable_name]['value'] = float(variable_val)
                        variables[variable_name]['data type'] = 'NUMBAR'
                        # variables[variable_name] = {'value': float(initial_value.strip()), 'data type': 'NUMBAR'}
                    elif re.match(boolean_pattern, variable_val):
                        variables[variable_name]['value'] = variable_val.strip()
                        variables[variable_name]['data type'] = 'TROOF'
                        # variables[variable_name] = {'value': initial_value.strip(), 'data type': 'TROOF'}
                    else:
                        if re.match(arithmetic_pattern, variable_val) or re.match(boolean_operation, variable_val) or re.match(comparison_pattern, variable_val):
                            #remove tokens using expression
                            is_var_assignment = True
                            filtered_tokens = [(value, category) for value, category in all_tokens if category not in expression]
                            new_value = arithmetic_analyzer(filtered_tokens, line_number, line)
                            
                            if re.match(integer_pattern, str(new_value)):
                                variables[variable_name] = {'value': int(new_value), 'data type': 'NUMBR'}
                            elif re.match(float_pattern, str(new_value)):
                                variables[variable_name] = {'value': float(new_value), 'data type': 'NUMBAR'}
                            elif re.match(boolean_pattern, str(new_value)):
                                variables[variable_name] = {'value': str(new_value), 'data type': 'TROOF'}
                            
                            # print("===================NEW VALUE==============", (new_value))
                            # print("line", line_number, ": call arithmetic function here to solve the val right away and store the result to the var initialized")
                        else:
                            variables[variable_name]['value'] = variable_val.strip()
                            variables[variable_name]['data type'] = 'YARN'
                            # variables[variable_name] = {'value': initial_value.strip(), 'data type': 'YARN'}
        else:
            print(f"Error in line {line_number}: Assignment error.")
            exit(0)

def if_else_statement(content, lines):
    global condition_index, if_else_condition
    
    if 'IT' not in variables:
        # print(if_else_condition)
        print(f"Error in line {if_else_condition[0][0]}: Accessing a null value.")
        exit(0)

    # check if the value of the key 'IT' in variables is equal to WIN
    if variables['IT']['value'] == 'WIN':
        # find the tuple with 'If Keyword'
        for i in range(len(if_else_condition)):
            if if_else_condition[i][1][0][1] == "If Keyword":
                # print("if", i+1)
                # condition_index = i+1
                condition_index.append(i+1)
                break
    else:
        for i in range(len(if_else_condition)):
            if if_else_condition[i][1][0][1] == "Else Keyword":
                # print("if", i+1)
                # condition_index = i+1
                condition_index.append(i+1)
                break
    if if_else_condition[condition_index[0]+1][1][0][1] != "If-Else or Switch-Case Delimiter" or if_else_condition[condition_index[0]+1][1][0][1] != "Else Keyword":
        # print("======If-Else or Switch-Case Delimiter")
        if variables['IT']['value'] == 'WIN':
            for i in range(condition_index[0]+1, len(if_else_condition)):
                # print("+", i, if_else_condition[i][1][0][1] )
                if if_else_condition[i][1][0][1] != "Else Keyword":
                    condition_index.append(i)
                
                else:
                    break
        else:
            for i in range(condition_index[0]+1, len(if_else_condition)):
                # print("+", i, if_else_condition[i][1][0][1] )
                if if_else_condition[i][1][0][1] != "If-Else or Switch-Case Delimiter":
                    condition_index.append(i)
                
                else:
                    break

    # print(condition_index, "\n\n")

    for inner_condition_index in condition_index:
    # similar format to lines 
        if_else_condition_newformat = [[item[0]] + item[1] if len(item) > 1 else [item[0]] for item in if_else_condition]
        removed_comment_cond = remove_comments(content[if_else_condition[inner_condition_index][0]-1], if_else_condition_newformat[inner_condition_index])
        
        # print("removed comment", if_else_condition_newformat[condition_index][1:])
        
        if if_else_condition[inner_condition_index][1][0][1] == 'Arithmetic Operator' or if_else_condition[inner_condition_index][1][0][1] == 'Boolean Operator' or if_else_condition[inner_condition_index][1][0][1] == 'Comparison Operator':
            b = arithmetic_analyzer(if_else_condition_newformat[inner_condition_index][1:], if_else_condition[inner_condition_index][0], lines)
            if b is not None:
                print("line",if_else_condition[inner_condition_index][0],": ", b)

            
        elif if_else_condition[inner_condition_index][1][0][1] == 'Output Keyword':
            b = print_analyzer(if_else_condition_newformat[inner_condition_index][1:], if_else_condition[inner_condition_index][0], lines)
            if b is not None:
                print("line",if_else_condition[inner_condition_index][0],": ", b)
        else:
            if if_else_condition[inner_condition_index][1][0][1] == 'Identifier':
            
            # print()   
                # analyze(content[condition_index], if_else_condition[condition_index][1][1][1], if_else_condition[condition_index][0], tokens[1:])
                # print("=======", if_else_condition[condition_index][1:][0])
                
                analyze(removed_comment_cond, if_else_condition[inner_condition_index][1][1][1], if_else_condition[inner_condition_index][0], if_else_condition[inner_condition_index][1:][0])
            else:
                analyze(removed_comment_cond,  if_else_condition[inner_condition_index][1][0][1], if_else_condition[inner_condition_index][0], if_else_condition[inner_condition_index][1:][0])

def loop_analyzer():
    global loop_lines, loop_tokens, if_keyword
    
    # print("HEREEEEEEEEEEEEEEEEEEEEEEEEE", loop_tokens[0][1][1:])
    print("================INSIDE LOOP================")
    # print(loop_lines)
    # print(variables)
    # Check if the syntax is correct
    if re.match(loop_pattern, loop_lines[0]):
        loop_match = re.match(loop_pattern, loop_lines[0])
        
        #Extract values from the matched groups
        loop_label = loop_match.group(1)
        loop_operation = loop_match.group(2)
        loop_variable = loop_match.group(3)
        repeat_keyword = loop_match.group(5) if loop_match.group(5) else None
        loop_expression = loop_match.group(6) if loop_match.group(6) else None
        loop_block = loop_lines[1:-1]
        loop_variable_end = loop_lines[-1].replace("IM OUTTA YR ", "")
        
        #check if loop expression has correct syntax
        #TO ADD
               
        #check if label is correct for ending loop delimeter
        if loop_variable_end.strip() == loop_label.strip():
            
            #check if variable is declared 
            if loop_variable in variables:
                #check if variable is osf type NUMBR
                if variables[loop_variable]['data type'] == "NUMBR":
                    #no errors, perform the loop operation 
                    loop_tokens_code = loop_tokens[1:-1]
                    
                    # print("HERE CORRECT", loop_variable)
                    # for lines in loop_tokens_code:
                    #     print("========Eto ba taena: ", lines[0])
                    #     print(loop_block)
                    # print("Loop Tokens======================", loop_tokens[0][1:])
                    # print("Loop Tokens======================", loop_tokens[1:-1])
                    
                    loop_variable_value = variables[loop_variable]['value']
                    loop_expression_tokens = []
                    found_til_or_wile = False
                    
                    #get the tokens of the loop expression
                    for item in loop_tokens[0][1][1:]:
                        if found_til_or_wile:
                            loop_expression_tokens.append(item)
                        elif isinstance(item, tuple) and (item[0] == 'TIL' or item[0] == 'WILE'):
                            found_til_or_wile = True

                    # print("EXPRESSION TOKENS=====", loop_expression_tokens)
                    
                    evaluate = arithmetic_analyzer(loop_expression_tokens, loop_tokens[0], loop_expression)
                    # print("HEREEEEEEEEEEEEE: ", evaluate)
                    # evaluate_expression = True
                    loop_block_counter = 0
                    is_GTFO = False
                    # print("evaluate_expression: ", evaluate_expression)
                                
                    #Execute the loop based on the operation and repeat condition
                    while (repeat_keyword == "TIL" and evaluate == "FAIL") or \
                          (repeat_keyword == "WILE" and evaluate == "WIN"):
                        
                        #Execute loop code block 
                        for loop_code_line in loop_tokens_code:
                            classification = loop_code_line[1][0][1]   
                            
                            # print("CLASSIFICATIONNNNNN:", classification)
                            if classification == "Break Keyword":
                                is_GTFO = True
                                break            
                                         
                            if classification == "Output Keyword":
                                b = print_analyzer(loop_code_line[1:][0], loop_code_line[0])
                                if b is not None:
                                    # print(loop_code_line[1:])
                                    print("THISSSSS",loop_code_line[0],": ", b)
                            if classification == "Arithmetic Operator" or classification == "Boolean Operator":
                                b = arithmetic_analyzer(loop_code_line[1:][0], loop_code_line[0], loop_block[loop_block_counter])
                                if b is not None:
                                    print("line", loop_code_line[0],": ", b)
                            if classification == "Function Call keyword":
                                function_analyzer(loop_block[loop_block_counter], loop_code_line[1:][0])
                            else:
                                # removed_comment = remove_comments(loop_block[loop_block_counter], loop_code_line)       
                                if loop_code_line[1][1] == 'Identifier':
                                    analyze(loop_block[loop_block_counter], classification, loop_code_line[0], loop_code_line[1:][0])
                                else:
                                    analyze(loop_block[loop_block_counter], classification, loop_code_line[0], loop_code_line[1:][0])

                            #increment loop code block line
                            loop_block_counter += 1
                        
                        #break loop if GTFO is encountered
                        if is_GTFO == True:
                            break
                        
                        loop_block_counter = 0
                        
                        #Perform the loop operation
                        if loop_operation == "UPPIN":
                            # print("UPPINNNNNN")
                            # print(variables[loop_variable]['value'])
                            # print("THIS IS WRONGGGGG", type(variables[loop_variable]['value']))
                            variables[loop_variable]['value'] += 1
                            # print(variables[loop_variable]['value'])
                        elif loop_operation == "NERFIN":
                            variables[loop_variable]['value'] -= 1
                                                
                        evaluate = arithmetic_analyzer(loop_expression_tokens, loop_tokens[0], loop_expression)

                else:
                    print(f"Error in line {loop_tokens[0][0]}: Variable '{loop_variable}' is not of type NUMBR.")
            else:
                print(f"Error in lineeeeee {loop_tokens[0][0]}: Variable '{loop_variable}' is not yet declared.")
        else:
            print(f"Error in line {loop_tokens[len(loop_tokens)-1][0]}: Label '{loop_variable_end}' does not match loop label '{loop_label}'.")
        
        # print("Label:", loop_label)
        # print("Operation:", loop_operation)
        # print("Variable:", loop_variable)
        # print("Repeat:", repeat_keyword)
        # print("Expression:", loop_expression)
        # print("Loop Block:", loop_block)
        # print("Loop_variable_end", loop_variable_end)
        # loop_variable_end = line.replace("IM OUTTA YR ", "")
    else:
        print(f"Error in line {loop_tokens[0][0]}: Incorrect format for loops.")
    
    # print(loop_lines)
    # print(loop_tokens)
    #Reset the necessary variables
    loop_lines = []
    loop_tokens = []

def variable_checker(var):
    if re.match(variable_pattern, var):
        return True
    else:
        return False

#This function checks the syntax of the function declarion.
#If there are no errors, the function is added to the global dictionary of functions        
def function_checker():
    global function_lines, function_tokens, functions
    
    function_match = re.match(function_pattern, function_lines[0])

    # Check if the syntax is correct
    if function_match:
        #check if function delimeter is correct
        if re.fullmatch(r'IF U SAY SO *', function_lines[len(function_lines)-1]):
            #extract from line
            function_name = function_match.group(1)
            function_parameters = [param for param in function_match.groups()[1:] if param is not None]
            function_tokens_code = function_tokens[1:-1]
            
            check_parameters = []
            
            #check for duplicate parameter names
            for params in function_parameters:
                if params in check_parameters:
                    print(f"Error in line {function_tokens[0][0]}: Parameter '{params}' already used.")
                else:
                    check_parameters.append(params)
            
            # #check if parameters follow correct naming convention
            # for parameter in function_parameters:
            #     if variable_checker(parameter) == False:
            #         print(f"Error in line {function_tokens[0][0]}: Parameter '{parameter}' is not correctly declared.")
            
            #check if the key is already in the dictionary
            #if no errors, add function to dictionary
            if function_name not in functions:
                functions[function_name] = [function_parameters, function_lines[1:-1], function_tokens_code]
                # print("\n", functions)
            else:
                print(f"Error in line {function_tokens[0][0]}: Function '{function_name}' already exists.")
        else:
            print(f"Error in line {function_tokens[len(function_tokens)-1][0]}: Incorrect syntax for function delimeter.")
    else:
        print(f"Error in line {function_tokens[0][0]}: Incorrect format for functions.")
    
    #reset the the lists
    function_lines = []
    function_tokens = []

def var_in_param(code_block_tuple, function_parameters):
    # print(function_parameters)
    for first, second in code_block_tuple:
        if second == "Identifier":
            if first not in function_parameters:
                return False, first
    return True, None
 
#This functions calls and evaluates the function given that there are no errors   
def function_analyzer(line, tokens):
    global variables, is_loop
    temp_variables = variables.copy()
    parameter_number = 0
    param_expressions = []
    

    combined_pattern_str = (
    arithmetic_pattern + '|' +
    comparison_pattern + '|' +
    smoosh_pattern_forfunc + '|' +
    boolean_pattern + '|' +
    literal_pattern + '|' +
    variable_pattern_forfunc
    )
    
    function_call_pattern = re.compile(
        r'I IZ ([a-zA-Z_][a-zA-Z_0-9]*)(?: YR ((?:' + combined_pattern_str + '))?(?: AN YR ((?:' + combined_pattern_str + '))?(?: AN YR ((?:' + combined_pattern_str + ')))?)?)? MKAY'
    )
    
    return_value = None
    has_return = False
    function_call_match = function_call_pattern.match(line)

    #check if syntax is correct
    if function_call_match:
        #extract from match
        function_name = function_call_match.group(1)

        #get parameters from line            
        # no parameters
        if len(tokens)-1 > 3:            
            for i in range(1, len(tokens)):
                if tokens[i][0] == 'YR':
                    parameter_number += 1
                if tokens[i][0] == 'AN':
                    if tokens[i][0] == 'YR':
                        parameter_number += 1
            next = 0
            temp = []    
            for i in range(parameter_number):
                if i == 0: 
                    for j in range(4, len(tokens)):
                        if (tokens[j][0] == 'AN' and tokens[j+1][0] == 'YR') or (tokens[j][0] == 'MKAY'):
                            next = j+2
                            param_expressions.append(' '.join(temp))
                            temp = []
                            break
                        else:
                            temp.append(tokens[j][0])
                else:
                    for k in range(next, len(tokens)):
                        if (tokens[k][0] == 'AN' and tokens[k+1][0] == 'YR') or (tokens[k][0] == 'MKAY'):
                            next = k+2
                            param_expressions.append(' '.join(temp))
                            temp = []
                            break
                        else:
                            temp.append(tokens[k][0])
        
        function_parameters = {}
        
        #check if function exists
        if function_name in functions:
            #access the function from the global function dictionary
            access_function = functions[function_name]
            access_function_params = access_function[0]
            param_counter = 0
            
            #check if the number of parameters match
            if len(param_expressions) == len(access_function[0]):
                #add parameters to a list
                for expression in param_expressions:
                    
                    parameter_name = access_function_params[param_counter]
                    data_type = get_data_type(expression)
                    
                    #add to dictionary if float, int, boolean, or string
                    if data_type in ("NUMBAR", "NUMBR", "TROOF", "YARN"):
                        if data_type == "NUMBAR": 
                            float(expression) 
                        elif data_type == "NUMBR": 
                            int(expression) 
                            
                        #add to dictionary
                        function_parameters[parameter_name] = {"value": expression, "data type": data_type}
                    else: 
                        #if expression or variable
                        
                        #check if variable or expression
                        if len(expression.split(" ")) > 1:
                            #if expression
                            
                            # Split the expression into tokens
                            expression_tokens = expression.split(" ")
                            expression_tokens_final = []
                            new_value = None
                            current_token = ""
                            tokens_dict = dict(tokens[1:])

                            #get the tokens of the expression
                            for expr in expression_tokens:
                                current_token += " " + expr
                                current_token = current_token.strip()

                                if current_token in tokens_dict:
                                    expression_tokens_final.append((current_token, tokens_dict[current_token]))      
                                    current_token = ""
                            
                            new_classification = expression_tokens_final[0][1]
                            
                            #evaluate the expression
                            if new_classification == "Arithmetic Operator" or new_classification == "Boolean Operator":
                                new_value = arithmetic_analyzer(expression_tokens_final, tokens[0], expression)
                                new_value = str(new_value)
                            else:
                                if new_classification == 'Identifier':
                                    new_value = analyze(expression, new_classification, tokens[0], expression_tokens_final)
                                else:
                                    new_value = analyze(expression, new_classification, tokens[0], expression_tokens_final)
                            
                            #get the data type of the evaluated expression
                            new_data_type = get_data_type(new_value)
                            if new_data_type in ("NUMBAR", "NUMBR", "TROOF", "YARN"):
                                if new_data_type == "NUMBAR": 
                                    float(new_value) 
                                elif new_data_type == "NUMBR": 
                                    int(new_value) 
                                    
                                #add to dictionary
                                function_parameters[parameter_name] = {"value": new_value, "data type": new_data_type}     
                        else:
                            # if variable
                            # check if variable exists
                            if expression in variables:
                                function_var_value = variables[expression]['value']
                                function_var_datatype = variables[expression]['data type']
                                function_parameters[parameter_name] = {"value": function_var_value, "data type": function_var_datatype}
                            else:
                                print(f"Error in line {tokens[0]}: Variable '{expression}' is not yet declared.") 
                                return
                    param_counter+=1
                
                variables = function_parameters
                line_counter = 0
                
                for code_block in access_function[2]:
                    # existing, no_var = var_in_param(code_block[1:][0], function_parameters)
                    
                    code_line = access_function[1][line_counter]
                    code_line_number = code_block[0]
                    code_tuples = code_block[1]
                    keyword = code_tuples[0][1]

                    # =============== RETURN ===============
                    if keyword == "Return Keyword": 
                        if len(code_tuples) > 1:
                        #remove "FOUND YR" from code line
                            code_line = access_function[1][line_counter].replace("FOUND YR ", "")
                            code_tuples = code_tuples[1:]
                            keyword = code_tuples[0][1]
                            has_return = True
                            
                            #if not expression
                            if len(code_tuples) == 1:
                                check_expression = get_data_type(code_line.strip())
                                if check_expression == "ELSE":
                                    # check if variable exist
                                    if code_line.strip() in variables:
                                        return_value = str(variables[code_line.strip()]['value']) 
                                    else:
                                        print(f"Error in line {code_line_number}: Variable '{code_line.strip()}' is not a function parameter.")
                                else:
                                    return_value = str(code_line.strip())
                                break
                        else:
                            if 'IT' not in temp_variables:
                                temp_variables['IT'] = {'value': None, 'data type': 'NOOB'}
                            else:
                                temp_variables['IT']['value'] = None
                                temp_variables['IT']['data type'] = 'NOOB'
                            break
                                
                    if keyword == "Break Keyword":
                        if 'IT' not in temp_variables:
                            temp_variables['IT'] = {'value': None, 'data type': 'NOOB'}
                        else:
                            temp_variables['IT']['value'] = None
                            temp_variables['IT']['data type'] = 'NOOB'
                        break
 
                    # =============== LOOPS ===============
                    if keyword == "Loop Start Delimiter":
                        is_loop = True
                    #add the loop code to a list
                    if is_loop == True:    
                        loop_lines.append(code_line)
                        loop_tokens.append([code_line_number, code_tuples])

                    #set is_loop to False and call loop analyzer
                    if keyword == "Loop End Delimiter":
                        is_loop = False
                        loop_analyzer()    

                    if not is_loop:
                        if keyword == "Output Keyword":
                            return_value = print_analyzer(code_tuples, code_line_number)
                        if keyword == "Arithmetic Operator" or keyword == "Boolean Operator":
                            return_value = arithmetic_analyzer(code_tuples, code_line_number, code_line)
                            return_value = str(return_value)
                        else:
                            if keyword == 'Identifier':
                                return_value = analyze(code_line, keyword, code_line_number, code_tuples)
                            else:
                                return_value = analyze(code_line, keyword, code_line_number, code_tuples)
                    
                    if has_return == True:
                        break
                    
                    line_counter+=1        
            else:
                print(f"Error in line {tokens[0]}: Number of parameters do not match.")
        else:
            print(f"Error in line {tokens[0]}: Function '{function_name}' not yet declared.")
    else:
        print(f"Error in line {tokens[0]}: Incorrect format for function call.")
    
    if has_return == True:
        #no error
        if return_value != None:
            
            return_value_type = get_data_type(return_value)
            if return_value_type in ("NUMBAR", "NUMBR", "TROOF", "YARN"):
                if return_value_type == "NUMBAR": 
                    float(return_value) 
                elif return_value_type == "NUMBR": 
                    int(return_value)                 
            if 'IT' not in temp_variables:
                temp_variables['IT'] = {'value': return_value, 'data type': return_value_type}
            else:
                temp_variables['IT']['value'] = return_value
                temp_variables['IT']['data type'] = return_value_type
    
    #reset the variables back
    variables = temp_variables
    
    return return_value

def switch_case_analyzer(content, lines):
    global switch_case_condition, temp, default_case_index
    # will be used if typecasting to int or float is needed
    # temp = 0
    # for i in range(len(switch_case_condition)):
    #     print("*",switch_case_condition[i])
    
    # print("\nswitch_case_condition", switch_case_condition)
    # print("\ncontent", content)
    # print("\nlines", lines)



    if 'IT' not in variables:
        # print(if_else_condition)
        print(f"Error in line {if_else_condition[0][0]}: Accessing a null value.")
        exit(0)

    

    match = re.match(literal_pattern, switch_case_condition[1][1][1][0])
    # this algo is for the OMG keyword where it will check if the value of IT is equal to the value literal
    # if variables['IT']['value'] == 'WIN':
    #     pass
    # match = literal_pattern.match(switch_case_condition[1][1][1][0])
    if match:
        # print("OK VALID FORMAT")
        if switch_case_condition[1][1][1][1] == "NUMBR Literal":
            temp = int(switch_case_condition[1][1][1][0])
        elif switch_case_condition[1][1][1][1] == "NUMBAR Literal":
            temp = float(switch_case_condition[1][1][1][0])
        else:
            temp = switch_case_condition[1][1][1][0]
        
        # print(type(temp))
        
        if temp == variables['IT']['value']:
            # print("check switch here",switch_case_condition[1][1][1][0], variables['IT']['value'])
            # if switch_case_condition[2][1][0][1] == "Arithmetic Operator" or  switch_case_condition[2][1][0][1] == "Boolean Operator":
            #     pass
            for i in range(2, len(switch_case_condition)):
                # print(switch_case_condition[i][1][0][1])
                if switch_case_condition[i][1][0][1] ==  "If-Else or Switch-Case Delimiter" or switch_case_condition[i][1][0][1] == "Break Keyword" or switch_case_condition[i][1][0][1] == "Default Case Keyword":
                    break
                else:
                    # print(i)
                    if switch_case_condition[i][1][0][1] == "Arithmetic Operator" or switch_case_condition[i][1][0][1] == "Boolean Operator":
                        # print(f'yooo {switch_case_condition[i][0]}')
                        b = arithmetic_analyzer(switch_case_condition[i][1][0:], switch_case_condition[i][0], lines)
                        
                        # print("check to pls", switch_case_condition[i][1][0:], switch_case_condition[i][0])
                        if b is not None:
                            print("line",switch_case_condition[i][0],": ", b)
                        # print("hereee", b)
                    elif switch_case_condition[i][1][0][1] == "Output Keyword":
                        b = print_analyzer(switch_case_condition[i][1][0:], switch_case_condition[i][0])
                        if b is not None:
                            print("line",switch_case_condition[i][0],": ", b)
                    else:
                        removed_comment = remove_comments(content[switch_case_condition[i][0]-1], switch_case_condition[i][1:])
                        # print("d222",removed_comment, switch_case_condition[i][1][0][1], switch_case_condition[i][0], switch_case_condition[i][1:])
                        # print(f'{removed_comment}\n{switch_case_condition[i][1][0][1]}\n{switch_case_condition[i][0]}\n{switch_case_condition[i][1][0:]}')
                        if switch_case_condition[i][1][0][1] == 'Identifier':
                            analyze(removed_comment, switch_case_condition[i][1][1][1], switch_case_condition[i][0], switch_case_condition[i][1][0:])
                        else:
                            analyze(removed_comment, switch_case_condition[i][1][0][1], switch_case_condition[i][0], switch_case_condition[i][1][0:])
                        # print(f'{removed_comment}\n{switch_case_condition[i][1][0][1]}\n{switch_case_condition[i][0]}\n{switch_case_condition[i][1][0:]}')


        else:
            default_case_index = None

            for i in range(len(switch_case_condition)):
                if switch_case_condition[i][1][0][1] == "Default Case Keyword":
                    default_case_index = i
                    break

            # print("heyy",default_case_index)
            # print("do the code block for omgwtf here")
            for i in range(default_case_index+1, len(switch_case_condition)):
                
                # print(switch_case_condition[i][1][0][1])
                if switch_case_condition[i][1][0][1] ==  "If-Else or Switch-Case Delimiter" or switch_case_condition[i][1][0][1] == "Break Keyword":
                    break
                else:
                    # print(i)
                    if switch_case_condition[i][1][0][1] == "Arithmetic Operator" or switch_case_condition[i][1][0][1] == "Boolean Operator":
                        # print(f'yooo {switch_case_condition[i][0]}')
                        b = arithmetic_analyzer(switch_case_condition[i][1][0:], switch_case_condition[i][0], lines)
                        
                        # print("check to pls", switch_case_condition[i][1][0:], switch_case_condition[i][0])
                        if b is not None:
                            print("line",switch_case_condition[i][0],": ", b)
                        # print("hereee", b)
                    elif switch_case_condition[i][1][0][1] == "Output Keyword":
                        b = print_analyzer(switch_case_condition[i][1][0:], switch_case_condition[i][0])
                        if b is not None:
                            print("line",switch_case_condition[i][0],": ", b)
                    else:
                        removed_comment = remove_comments(content[switch_case_condition[i][0]-1], switch_case_condition[i][1:])
                        # print("d222",removed_comment, switch_case_condition[i][1][0][1], switch_case_condition[i][0], switch_case_condition[i][1:])
                        # print(f'{removed_comment}\n{switch_case_condition[i][1][0][1]}\n{switch_case_condition[i][0]}\n{switch_case_condition[i][1][0:]}')
                        if switch_case_condition[i][1][0][1] == 'Identifier':
                            analyze(removed_comment, switch_case_condition[i][1][1][1], switch_case_condition[i][0], switch_case_condition[i][1][0:])
                        else:
                            analyze(removed_comment, switch_case_condition[i][1][0][1], switch_case_condition[i][0], switch_case_condition[i][1][0:])
                        # print(f'{removed_comment}\n{switch_case_condition[i][1][0][1]}\n{switch_case_condition[i][0]}\n{switch_case_condition[i][1][0:]}')
            # default_case_index = None

    else:
        # for i in range(len(switch_case_condition)):
        #     print("*",switch_case_condition[i])
        print(f"Error in line {switch_case_condition[1][0]}: Invalid value format for OMG. Value must only be a yarn, troof, numbr, or numbar.")
        exit(0) 

#TOKENIZE INPUTTED CODE
def tokenize(content):
    global to_remove, if_delimiter, oic_found, if_keyword,else_keyword, inside_wazzup_buhbye, if_else_condition, wazzup_line, condition_index 
    global loop_lines, is_loop, is_function, function_lines, loop_tokens, function_tokens
    global switch_delimiter, switch_case_condition, temp, default_case_index, case_keyword, default_case_keyword

    all_tokens = []
    
    # multiple_index = []

    # Remove empty strings from the list
    filtered_list = [item for item in content if item != ""]
    # print(filtered_list)
    #check if the lol code starts with HAI and ends with KTHXBYE
    # if filtered_list[0] != "HAI":
    if not re.fullmatch(r'HAI *', filtered_list[0]):
        print(f'Error: Code delimiter not existing. Should start with HAI')
        exit(0)     
    # if filtered_list[len(filtered_list)-1] != "KTHXBYE":
    if not re.fullmatch(r'KTHXBYE *', filtered_list[len(filtered_list)-1]):
        print(f'Error: Code delimiter not existing. Should end with KTHXBYE')
        exit(0)  
        
    multi_line = False
    line_number = 1
    initial_multiline = True
    inserted = False
    current_line_r = 0
    
    for lines in content:
        # print("ok",lines)
        tokens = []
        tokens.append(line_number)
        next_line = 0
        lines_split = lines.strip().split(" ")
        # print("===", lines_split)
        potential = False
        last = lines_split[-1]
        
        if(multi_line == False):
            to_check = ""

        # print(last)
        if(next_line == 0):
            for word in lines_split:
                #check if last word
                if(word == last):
                    next_line = 1
                    
                if(to_check == ""):
                    to_check = word
                else:
                    to_check = to_check + " " +  word 
                
                for key, value in keywords.items():
                    if to_check == key:
                        # print("======================TOCHECK:", to_check, line_number)
                        
                        #if current to_check is R
                        if to_check == "R":
                            current_line_r = line_number
                        
                        if line_number!=1 and line_number==current_line_r:
                            if to_check == "MAEK": 
                                # print("=============R MAEKK========")
                                tokens.append(("R MAEK", "Reassignment Operator"))
                                
                                # #pop the tuple with R from the tokens 
                                tokens.remove(("R", "Assignment Operator"))
                                to_check = ""
                                break
                                
                        tokens.append((key, value))   
                        to_check = ""
                        potential = False
                        break
                    
                #check if the current string is a potential keyword
                if(to_check in potential_keyword):
                    potential = True
                
                # Check if the string matches any key in the dictionary
                if(potential == True):
                    for key, value in keywords.items():
                        if to_check == key:
                            tokens.append((key, value))
                            to_check = ""
                            potential = False
                            break
                        
                if(potential == False):   
                    #check if single line comment
                    if re.search(r'^\s*BTW\b', to_check):
                        if(next_line == 1):
                            tokens.append(("BTW", "Single Line Comment Declaration"))
                            if to_check.strip() != "BTW":
                                tokens.append((to_check.replace("BTW ", ""), "Single Line Comment"))
                        continue
                    
                    #check if multi-line comment
                    if re.search(r'OBTW\b', to_check):
                        multi_line = True
                        if initial_multiline:
                            tokens.append(("OBTW", "Multi-Line Comment Declaration"))
                            if next_line == 1 and not to_check != r'OBTW\b':
                                tokens.append((to_check.replace("OBTW ", ""), "Multi-Line Comment"))
                                inserted = True
                                # to_check = "OBTW "
                            line_before = to_check
                            initial_multiline = False
                        else:
                            if to_check.find("TLDR") != -1:
                                modified_string = to_check.replace("OBTW", "").replace("TLDR", "")
                                found = False
                                
                                #find if the the comment is included
                                for inner_list in all_tokens:
                                    for element in inner_list[1:]:  # Skip the first element (integer)
                                        if any(isinstance(item, str) and modified_string in item for item in element):
                                            found = True
                                            break
                                        
                                if not found and not inserted:
                                    tokens.append((modified_string.strip(), "Multi-Line Comment"))

                                tokens.append(("TLDR", "Multi-Line Comment Delimiter"))
                                multi_line = False
                                initial_multiline = True
                                inserted = False
                                to_check = ""
                            else:
                                if(next_line == 1):
                                    tokens.append((to_check.replace(line_before, "").strip(), "Multi-Line Comment"))
                                    inserted = True
                                    line_before = to_check
                        continue

                    #check if it is a string literal
                    if re.match(string_literal, to_check):
                        tokens.append((to_check, "String Literal"))
                        to_check = ""
                    
                    #check if it is a bool
                    if re.match(bool_literal, to_check):
                        tokens.append((to_check, "Boolean"))
                        to_check = ""
                    
                    #check if it is a type literal
                    if re.match(type_literal, to_check):
                        tokens.append((to_check, "Type Literal"))
                        to_check = ""
                    
                    if re.match(literals[0], to_check):
                        tokens.append((to_check, "NUMBR Literal"))
                        to_check = ""
                        
                    if re.match(literals[1], to_check):
                        tokens.append((to_check, "NUMBAR Literal"))
                        to_check = ""
                        
                    if re.match(identifier, to_check):
                        tokens.append((to_check, "Identifier"))
                        to_check = ""
            # print("HEREEEEEEEEEEEEEEEEE:")
            # print(tokens)
            # # line_number += 1
            # # all_tokens.append(tokens)
                    
            #check if tokens is not empty and there are no comment errors
            if len(tokens) > 1 and not check_comment_errors(lines, line_number):
                
                #remove comments from the tuple of lexemes
                if tokens[1][1] not in to_remove:
                    removed_tuple = [tup for tup in tokens[1:] if tup[1] not in to_remove]
                    # print("REMOVEDDDDD!", tokens[1][1])
                # else:
                #     print("")
                #     removed_tuple = tokens[1]
                # print("ETOOOOOO:",removed_tuple)

                # checks if the if else or switch case has delimiter
                if re.match(oic_pattern, removed_tuple[0][0]):
                    oic_found = True

                if if_delimiter == True:
                    if removed_tuple[0][0] == "KTHXBYE" and oic_found == False:
                        print("Error in line ", line_number, ": If-Else or Switch-Case Delimiter not found.")
                        exit(0)
                    if removed_tuple[0][0] == "OIC":
                        if_else_condition.append([tokens[0], removed_tuple])
                        if_else_statement(content, lines)

                        # for i in range(len(if_else_condition)):
                        #     print("*",if_else_condition[i])

                        condition_index = []
                        if_delimiter = False
                        oic_found = False
                        if_else_condition = []

                        # print(condition_index, if_delimiter, oic_found)

                    if_else_condition.append([tokens[0], removed_tuple])

                elif switch_delimiter == True:
                    if removed_tuple[0][0] == "KTHXBYE" and oic_found == False:
                        print("Error in line ", line_number, ": If-Else or Switch-Case Delimiter not found.")
                        exit(0)
                    else:
                        if removed_tuple[0][0] == "OIC":
                            switch_case_condition.append([tokens[0], removed_tuple])
                            switch_case_analyzer(content, lines)
                            

                            switch_delimiter = False
                            oic_found = False
                            switch_case_condition = []
                            temp = 0
                            default_case_index = 0
                    
                    switch_case_condition.append([tokens[0], removed_tuple])
                else:
                    # print(tokens[1][0])
                    removed_comment = remove_comments(lines, tokens)
                    
                    #=======================LOOPS=======================
                    if tokens[1][0] == "IM IN YR" and is_function == False:
                        is_loop = True
                    
                    #add the loop code to a list
                    if is_loop == True:    
                        loop_lines.append(removed_comment)
                        loop_tokens.append([line_number, removed_tuple])
                        # continue
                    
                    #set is_loop to False and call loop analyzer
                    if tokens[1][0] == "IM OUTTA YR" and is_function == False:
                        # print("Pumasok baaaaaaaaaaaaaa")
                        is_loop = False
                        loop_analyzer()
                    
                    #=======================FUNCTION=======================

                    if tokens[1][0] == "HOW IZ I":
                        # print('ETO  BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                        is_function = True
                    
                    #add the function code to a list
                    if is_function == True:
                        # print('ETO  BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', is_function)
                        function_lines.append(removed_comment)
                        function_tokens.append([line_number, removed_tuple])
                        # continue
                    
                    #set is_function to False and call function analyzer
                    if tokens[1][0] == "IF U SAY SO":
                        # print('ETO  BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA if you say', is_function)
                        is_function = False
                        function_checker()
                    
                    if tokens[1][0] == "I IZ":
                        function_analyzer(removed_comment, tokens)
                    
                    if is_function or is_loop == True:
                        line_number += 1
                        all_tokens.append(tokens)
                        continue
                    
                    #=======================ARITHMETIC OPERATIONS=======================    
                    if tokens[1][1] == "Arithmetic Operator" or tokens[1][1] == "Boolean Operator" or tokens[1][1] == "Comparison Operator":

                        # this is to ensure that the wazzup and buhbye block only contains variable declaration 
                        # also, this checks whether the wazzup has corresponding buhbye, and vice versa
                        
                        
                        b = arithmetic_analyzer(removed_tuple, tokens[0], lines)
                        #print("ETOOOOOOOOOOOOOO")
                        #print("removed_tuple", removed_tuple)
                        #print("tokens[0]", tokens[0])
                        #print("lines", lines)
                        if b is not None:
                            print("line",tokens[0],": ", b)
                    elif tokens[1][1] == "Output Keyword":
                        b = print_analyzer(removed_tuple, tokens[0])
                        if b is not None:
                            print("line",tokens[0],": ", b)
                    # this is a condition when if keyword is found but no if delimiter  
                    elif tokens[1][1] == "If Keyword":
                        if_keyword = True
                        if if_delimiter == False:
                            print(f"Error in line {line_number}: No If Delimiter found.")
                            exit(0)
                    elif tokens[1][1] == "Else Keyword":
                        else_keyword = True
                        if if_delimiter == False:
                            print(f"Error in line {line_number}: No If Delimiter found.")
                            exit(0)
                    # sets the flag to true when if delimiter is found
                    elif tokens[1][1] == "If Delimiter":
                        if_else_condition.append([tokens[0], removed_tuple])
                        if_delimiter = True
                    elif tokens[1][1] == "Case Keyword":
                        case_keyword = True
                        if switch_delimiter == False:
                            print(f"Error in line {line_number}: No Switch-Case Delimiter found.")
                            exit(0)
                    elif tokens[1][1] == "Default Case Keyword":
                        default_case_keyword = True
                        if switch_delimiter == False:
                            print(f"Error in line {line_number}: No Switch-Case Delimiter found.")
                            exit(0)
                    elif tokens[1][1] == "Switch-Case Delimiter":
                        switch_case_condition.append([tokens[0], removed_tuple])
                        # print("switchhh",tokens[0], removed_tuple)
                        switch_delimiter = True
                    else:
                        # removed_comment = remove_comments(lines, tokens)
                        # print("check no comment", removed_comment)
                        if tokens[1][1] == 'Identifier':
                            # print()
                            analyze(removed_comment, tokens[2][1], tokens[0], tokens[1:])
                        else:
                            analyze(removed_comment, tokens[1][1], tokens[0], tokens[1:])

            line_number += 1
            all_tokens.append(tokens)

    return all_tokens

def main():
    file_name_lol = False
    file_name = ""

    while not file_name_lol:
        # file_name = input("Enter filename: ")
        file_name = "try.lol"

        if(file_name[-4:] == ".lol"):
            file_name_lol = True
    
    #get the contents of the lol code
    content = readFile(file_name)

    tokens = tokenize(content)
    


    # print(tokens)
    # for i in range(len(tokens)):
    #     print(tokens[i])
    

    # for line in tokens:
    #     print(line)

    print("\n====================VARIABLES====================")
    for key, value in variables.items():
        print(f"{key}\n\tValue: {value['value']}, Data Type: {value['data type']}")
    print("\n")

    # print("\n====================Tokens====================")
    # for token in tokens:
    #     print(token)
    
    # print('thisssssssssssssssssssssssssssssssssssssssss')
    # print(variables)
    
    # print('functionsssssss')

    # for func in functions.items():
    #     print(func)

    # print("\n====================LEXEME====================")
    # print("LEXEME\t\t\tIDENTIFIER")
    
    # # #get only the tuples from the list
    # only_tuples = [item for sublist in tokens for item in sublist if isinstance(item, tuple)]
    
    # # #get the max width of each column
    # col_wid = [max(map(len, map(str, col))) for col in zip(*only_tuples)]

    # for row in only_tuples:
    #     print("\t\t\t".join(str(value).ljust(width) for value, width in zip(row, col_wid))) 

main()