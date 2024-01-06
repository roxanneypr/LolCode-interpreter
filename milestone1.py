#Authors:
    # Gadil, Jea Anne
    # Leyco, Charlize Althea
    # Resuello, Roxanne Ysabel

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
import re


    
    
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
    return contents

# Milestone 1 - lexical analyzer
#===========================================================

# Keywords dictionary
keywords = {
    "HAI" : "Code Delimiter"
    , "KTHXBYE" : "Code Delimiter"
    , "BTW" : "Single Line Comment Declaration"
    , "OBTW" : "Multi-Line Comment Delimiter"
    , "TLDR" : "Multi-Line Comment Delimiter"
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
    , "^WTF\?$" : "Switch-Case Delimiter"
    , "OMG" : "Case Keyword"
    , "OMGWTF" : "Default Case Keyword"
    , "IM IN YR" : "Loop Delimiter"
    , "GTFO" : "Break Keyword"
    , "UPPIN" : "Increment Operator"
    , "NERFIN" : "Decrement Operator"
    , "YR" : "Loop Separator"
    , "TIL" : "FAIL Loop Repeater"
    , "WILE" : "WIN Loop Repeater"
    , "IM OUTTA YR" : "Loop Delimiter"
    , "HOW IZ I" : "Function Delimiter"
    , "IF U SAY SO" : "Function Delimiter"
    # ADDED
    , "WAZZUP" : "Variable Keyword"
    , "BUHBYE" : "Variable Keyword"
    , "FOUND YR": "Return Keyword"
    , "I IZ": "Function Call keyword"
}

# Regex for identifier
identifier = "^[a-zA-Z][a-zA-Z0-9_]*$"

# Regex for NUMBR/NUMBAR (number) literals
literals = ["^-?\d+$", "^-?\d*\.\d+$"]

# Regex for YARN (string) literals
string_literal = "^\"[^”]*\"$"

# Regex for TROOF (bool) literals
bool_literal = "(WIN|FAIL)"

# Regex for TYPE literals
type_literal = "(NOOB|TROOF|NUMBAR|NUMBR|YARN)"

# Potential keywords array
potential_keyword = ["I", "I HAS", "SUM", "DIFF", "PRODUKT", "QUOSHUNT", "MOD"
                    , "BIGGR", "SMALLR", "BOTH", "EITHER", "WON", "ANY", "ALL"
                    , "IS", "IS NOW", "O", "YA", "NO", "IM", "IM IN", "IM OUTTA"
                    , "HOW", "HOW IZ", "IF", "IF U", "IF U SAY"]

#TOKENIZE INPUTTED CODE
def tokenize(content):
    tokens = []

    # Remove empty strings from the list
    filtered_list = [item for item in content if item != ""]

    for lines in filtered_list:
        #print(lines)
        lines_split = lines.strip().split(" ")
        to_check = ""
        potential = False
        for word in lines_split:
            if(to_check == ""):
                to_check = word
            else:
                to_check = to_check + " " +  word 
            
            
            for key, value in keywords.items():
                if to_check == key:
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

                    # #check if it is an identifier
                    # if re.match(identifier, to_check):
                    #     tokens.append((to_check, "Identifier"))
                    #     to_check = ""
                    #     print(to_check)

    #print(tokens)

    return tokens

def show_content(file_path, self):

        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                
        self.code_editor.text_widget.delete("1.0", tk.END)
        self.code_editor.text_widget.insert(tk.END, content)
        return

class CodeEditor(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=1, column=0, sticky="nsew")
        self.label = tk.Label(self, text="Text Editor")
        self.label.pack()

        self.text_widget = tk.Text(self, wrap="word", undo=True)
        self.text_widget.pack(fill="both", expand=True)

class LexemeTable(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=1, column=1, sticky="nsew")
        self.label = tk.Label(self, text="Lexeme Table")
        self.label.pack()

        self.treeview = ttk.Treeview(self)
        self.treeview["columns"] = ("Lexeme", "Classification")
        self.treeview.heading("Lexeme", text="Lexeme")
        self.treeview.column("Lexeme", anchor="w", width=150)  # Adjusted anchor to "w"
        self.treeview.heading("Classification", text="Classification")
        self.treeview.column("Classification", anchor="w", width=200)  # Adjust width as needed
        self.treeview.pack(fill="both", expand=True)

    def populate(self, lexeme_list):
        for idx, (lexeme, category) in enumerate(lexeme_list, start=1):
            self.treeview.insert("", idx, values=(lexeme, category))



class SymbolTable(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=1, column=2, sticky="nsew")
        self.label = tk.Label(self, text="Symbol Table")
        self.label.pack()
        self.treeview = ttk.Treeview(self)
        self.treeview["columns"] = ("Identifier", "Value")
        self.treeview.heading("Identifier", text="Identifier")
        self.treeview.column("Identifier", anchor="center", width=100)
        self.treeview.heading("Value", text="Value")
        self.treeview.column("Value", anchor="center", width=100)
        self.treeview.pack(fill="both", expand=True)

class Console(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=2, column=0, columnspan=3, sticky="nsew")
        self.label = tk.Label(self, text="Console")
        self.label.pack()
        self.text_widget = tk.Text(self, wrap="word", state="normal")
        self.text_widget.pack(fill="both", expand=True)
        self.execute_button = tk.Button(self, text="Execute", command=self.execute_code)
        self.execute_button.pack()

    def execute_code(self):
        code = self.text_widget.get("1.0", tk.END)
        print(f"Executing code:\n{code}")

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tokens = []
        self.title("Code Editor with Lexemes and Symbol Table")

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.select_file_button = tk.Button(self, text="Select File", command=self.load_file)
        self.select_file_button.grid(row=0, column=0, columnspan=3, sticky="nsew")

        self.code_editor = CodeEditor(self)
        self.lexeme_table = LexemeTable(self)
        self.symbol_table = SymbolTable(self)
        self.console = Console(self)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.lol"), ("All files", "*.*")])
        contents = []
        if file_path:
            with open(file_path, "r") as file:
                for lines in file:
                    contents.append(lines.replace("\n", ""))

        self.code_editor.text_widget.delete("1.0", tk.END)
        self.code_editor.text_widget.insert(tk.END, "\n".join(contents))
        self.tokens = tokenize(contents)

        # Update LexemeTable with the new tokens
        self.lexeme_table.populate(self.tokens)

if __name__ == "__main__":
    app = Application()
    app.mainloop()