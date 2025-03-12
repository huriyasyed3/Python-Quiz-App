import streamlit as st 
import random
import pandas as pd 

st.title("🎯 Python Quiz Hub")

# Questions Dictionary by Chapter
quiz_data = {
   "Google Colab": [
    {"question": "What is Google Colab used for?", "options": ["Web development", "Machine Learning & Data Science", "Game Development", "Cyber Security"], "answer": "Machine Learning & Data Science"},
    {"question": "Which programming language is primarily used in Google Colab?", "options": ["Java", "C++", "Python", "JavaScript"], "answer": "Python"},
    {"question": "What is the file extension for Google Colab notebooks?", "options": [".ipynb", ".py", ".txt", ".csv"], "answer": ".ipynb"},
    {"question": "Does Google Colab provide free GPU access?", "options": ["Yes", "No"], "answer": "Yes"},
    {"question": "Which cloud service does Google Colab integrate with?", "options": ["AWS", "Google Drive", "Azure", "Dropbox"], "answer": "Google Drive"},
    {"question": "Which type of Jupyter notebook environment does Google Colab provide?", "options": ["Local", "Cloud-based", "Offline", "Hybrid"], "answer": "Cloud-based"},
    {"question": "Which library is pre-installed in Google Colab?", "options": ["numpy", "pandas", "tensorflow", "All of the above"], "answer": "All of the above"},
    {"question": "How can you install additional Python packages in Google Colab?", "options": ["install()", "pip install", "setup()", "load_package()"], "answer": "pip install"},
    {"question": "What is the maximum runtime for free GPU usage in Google Colab?", "options": ["8 hours", "12 hours", "24 hours", "Unlimited"], "answer": "12 hours"},
    {"question": "Which shortcut is used to run a cell in Google Colab?", "options": ["Shift + Enter", "Ctrl + Enter", "Alt + Enter", "All of the above"], "answer": "All of the above"},
    {"question": "How do you upload files in Google Colab?", "options": ["colab.upload()", "files.upload()", "import.upload()", "drive.upload()"], "answer": "files.upload()"},
    {"question": "How do you mount Google Drive in Colab?", "options": ["drive.mount('/content/drive')", "mount.drive()", "colab.mount_drive()", "connect.drive()"], "answer": "drive.mount('/content/drive')"},
    {"question": "Which magic command is used to check the current working directory in Google Colab?", "options": ["%cwd", "%pwd", "!dir", "%ls"], "answer": "%pwd"},
    {"question": "How do you list the files in a directory using a Colab cell?", "options": ["ls", "!ls", "dir()", "%list"], "answer": "!ls"},
    {"question": "Which Colab runtime type allows you to use a TPU?", "options": ["Standard", "GPU", "TPU", "Custom"], "answer": "TPU"},
    {"question": "What does Google Colab use to execute Python code?", "options": ["Jupyter Notebook", "Google's Custom Engine", "PyCharm", "Anaconda"], "answer": "Jupyter Notebook"},
    {"question": "How do you restart the runtime in Google Colab?", "options": ["Kernel -> Restart", "Runtime -> Restart runtime", "Tools -> Restart", "File -> Restart"], "answer": "Runtime -> Restart runtime"},
    {"question": "Which of the following is a unique feature of Google Colab?", "options": ["Free cloud storage", "Free GPU access", "Integration with Google Drive", "All of the above"], "answer": "All of the above"},
    {"question": "How do you clear the output of a cell in Google Colab?", "options": ["Clear()", "Runtime -> Clear Output", "Cell -> Clear Output", "Kernel -> Clear Output"], "answer": "Runtime -> Clear Output"},
    {"question": "Which command is used to install TensorFlow in Google Colab?", "options": ["install tensorflow", "!pip install tensorflow", "import tensorflow", "#install tensorflow"], "answer": "!pip install tensorflow"}
],

  "Python Basics": [
    {"question": "Who developed Python?", "options": ["James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup"], "answer": "Guido van Rossum"},
    {"question": "What type of programming language is Python?", "options": ["Compiled", "Interpreted", "Assembly", "Machine Language"], "answer": "Interpreted"},
    {"question": "Which year was Python released?", "options": ["1989", "1991", "2000", "2008"], "answer": "1991"},
    {"question": "Which symbol is used to start a comment in Python?", "options": ["//", "#", "<!--", "/*"], "answer": "#"},
    {"question": "Which of the following is not a valid Python identifier?", "options": ["my_var", "2var", "_var", "Var123"], "answer": "2var"},
    {"question": "What is the extension of a Python file?", "options": [".py", ".python", ".pyt", ".pt"], "answer": ".py"},
    {"question": "Which function is used to display output in Python?", "options": ["print()", "display()", "echo()", "show()"], "answer": "print()"},
    {"question": "Which function is used to take user input in Python?", "options": ["input()", "scan()", "read()", "get()"], "answer": "input()"},
    {"question": "Which keyword is used to define a function in Python?", "options": ["function", "def", "define", "fn"], "answer": "def"},
    {"question": "Which of the following is a correct way to declare a variable in Python?", "options": ["x = 10", "int x = 10", "var x = 10", "x : 10"], "answer": "x = 10"},
    {"question": "How do you check the data type of a variable in Python?", "options": ["typeof()", "type()", "checktype()", "datatype()"], "answer": "type()"},
    {"question": "Which keyword is used to create a loop in Python?", "options": ["repeat", "while", "loop", "iterate"], "answer": "while"},
    {"question": "Which of the following is not a valid data type in Python?", "options": ["int", "float", "double", "bool"], "answer": "double"},
    {"question": "How do you start a multi-line comment in Python?", "options": ["/*", "//", "#", '"""'], "answer": '"""'},
    {"question": "Which module is used for mathematical operations in Python?", "options": ["math", "cmath", "random", "statistics"], "answer": "math"},
    {"question": "Which operator is used for integer division in Python?", "options": ["/", "//", "%", "**"], "answer": "//"},
    {"question": "Which of the following is used to define a block of code in Python?", "options": ["{}", "()", "[]", "Indentation"], "answer": "Indentation"},
    {"question": "What will `print(2 ** 3)` output?", "options": ["5", "6", "8", "9"], "answer": "8"},
    {"question": "How do you write an empty function in Python?", "options": ["def func(): pass", "def func(): {}", "def func(): return", "def func(): end"], "answer": "def func(): pass"},
    {"question": "Which statement is used to terminate a loop in Python?", "options": ["exit", "stop", "break", "terminate"], "answer": "break"}
],

   "Data Types": [
    {"question": "Which of the following is an immutable data type?", "options": ["List", "Dictionary", "Tuple", "Set"], "answer": "Tuple"},
    {"question": "What function is used to check the type of a variable?", "options": ["typeof()", "type()", "gettype()", "varType()"], "answer": "type()"},
    {"question": "Which data type is used to store multiple values in a single variable?", "options": ["int", "list", "bool", "str"], "answer": "list"},
    {"question": "Which Python data type represents True/False values?", "options": ["Boolean", "Integer", "String", "Float"], "answer": "Boolean"},
    {"question": "How do you define a dictionary in Python?", "options": ["{}", "[]", "()", "<>"], "answer": "{}"},
    {"question": "Which of the following is a mutable data type?", "options": ["String", "Tuple", "List", "Integer"], "answer": "List"},
    {"question": "What will be the output of type(5.5)?", "options": ["int", "float", "double", "number"], "answer": "float"},
    {"question": "Which data type can hold key-value pairs?", "options": ["Set", "List", "Dictionary", "Tuple"], "answer": "Dictionary"},
    {"question": "What is the default data type of an input() function in Python?", "options": ["int", "float", "str", "bool"], "answer": "str"},
    {"question": "Which data type is used for storing unordered and unique values?", "options": ["List", "Tuple", "Set", "Dictionary"], "answer": "Set"},
    {"question": "Which of the following data types supports indexing?", "options": ["List", "Tuple", "String", "All of the above"], "answer": "All of the above"},
    {"question": "How do you declare a tuple with one element?", "options": ["(1)", "(1,)", "{1}", "[1]"], "answer": "(1,)"},
    {"question": "Which data type is used to represent whole numbers in Python?", "options": ["int", "float", "bool", "str"], "answer": "int"},
    {"question": "Which function converts a value into an integer?", "options": ["int()", "float()", "str()", "bool()"], "answer": "int()"},
    {"question": "Which of the following data types allows duplicate values?", "options": ["Set", "List", "Dictionary", "Both List and Dictionary"], "answer": "Both List and Dictionary"},
    {"question": "What will type(None) return?", "options": ["NoneType", "Null", "None", "Empty"], "answer": "NoneType"},
    {"question": "Which data type is best suited for representing text?", "options": ["int", "str", "bool", "list"], "answer": "str"},
    {"question": "How do you create an empty set in Python?", "options": ["{}", "set()", "[]", "set[]"], "answer": "set()"},
    {"question": "Which of the following can store both integers and strings?", "options": ["List", "Tuple", "Dictionary", "All of the above"], "answer": "All of the above"},
    {"question": "Which function converts a value into a string?", "options": ["str()", "int()", "float()", "bool()"], "answer": "str()"}
],

"Operators, Keywords, Variables": [
    {"question": "Which operator is used for exponentiation in Python?", "options": ["*", "**", "//", "^"], "answer": "**"},
    {"question": "Which keyword is used to define a variable in Python?", "options": ["var", "let", "const", "No keyword is needed"], "answer": "No keyword is needed"},
    {"question": "What does the '==' operator do?", "options": ["Assigns a value", "Compares two values", "Bitwise AND", "Logical NOT"], "answer": "Compares two values"},
    {"question": "Which keyword is used to define a function?", "options": ["func", "define", "def", "function"], "answer": "def"},
    {"question": "What will '5//2' return in Python?", "options": ["2.5", "2", "3", "5"], "answer": "2"},
    {"question": "Which operator is used for integer division?", "options": ["/", "//", "%", "**"], "answer": "//"},
    {"question": "Which keyword is used to declare a constant in Python?", "options": ["const", "final", "static", "No specific keyword"], "answer": "No specific keyword"},
    {"question": "Which symbol is used for the modulus operator?", "options": ["%", "//", "**", "&"], "answer": "%"},
    {"question": "What will '3 * 2 ** 3' evaluate to?", "options": ["24", "18", "64", "9"], "answer": "24"},
    {"question": "Which keyword is used to import a module in Python?", "options": ["include", "import", "require", "fetch"], "answer": "import"},
    {"question": "Which of the following is a valid variable name?", "options": ["2var", "var_2", "var-2", "var 2"], "answer": "var_2"},
    {"question": "Which keyword is used to define a class?", "options": ["class", "Class", "define", "object"], "answer": "class"},
    {"question": "Which operator is used for logical AND?", "options": ["&", "&&", "and", "AND"], "answer": "and"},
    {"question": "Which operator is used for assignment?", "options": ["=", "==", ":=", "==="], "answer": "="},
    {"question": "What will '10 % 3' return?", "options": ["1", "3", "0", "10"], "answer": "1"},
    {"question": "Which of the following is a **valid** Python keyword?", "options": ["switch", "case", "pass", "goto"], "answer": "pass"},
    {"question": "What will 'bool(0)' return?", "options": ["True", "False", "None", "Error"], "answer": "False"},
    {"question": "Which keyword is used to handle exceptions in Python?", "options": ["catch", "handle", "try", "except"], "answer": "try"},
    {"question": "Which of the following is an identity operator?", "options": ["==", "!=", "is", "in"], "answer": "is"},
    {"question": "Which of the following is a membership operator?", "options": ["in", "not in", "is", "both A & B"], "answer": "both A & B"}
],

"Strings & Type Casting": [
    {"question": "How do you convert an integer to a string?", "options": ["str()", "int()", "float()", "bool()"], "answer": "str()"},
    {"question": "Which method is used to remove whitespace from both ends of a string?", "options": ["trim()", "strip()", "remove()", "clean()"], "answer": "strip()"},
    {"question": "What will 'Hello' + 'World' return?", "options": ["HelloWorld", "Hello World", "Error", "Hello+World"], "answer": "HelloWorld"},
    {"question": "What is string slicing?", "options": ["Dividing a string", "Extracting part of a string", "Sorting characters", "Joining strings"], "answer": "Extracting part of a string"},
    {"question": "Which function returns the length of a string?", "options": ["count()", "len()", "size()", "length()"], "answer": "len()"},
    {"question": "How do you convert a string to an integer?", "options": ["str()", "int()", "float()", "bool()"], "answer": "int()"},
    {"question": "Which operator is used for string concatenation?", "options": ["+", "-", "*", "/"], "answer": "+"},
    {"question": "Which method converts all characters in a string to uppercase?", "options": ["upper()", "capitalize()", "toUpper()", "casefold()"], "answer": "upper()"},
    {"question": "What does the isdigit() method do?", "options": ["Checks if all characters are digits", "Converts string to integer", "Removes non-numeric characters", "Counts digits in string"], "answer": "Checks if all characters are digits"},
    {"question": "What will print(type('5')) return?", "options": ["int", "str", "float", "bool"], "answer": "str"},
    {"question": "Which function is used to find a substring in a string?", "options": ["find()", "search()", "index()", "locate()"], "answer": "find()"},
    {"question": "Which method replaces a substring within a string?", "options": ["replace()", "swap()", "change()", "modify()"], "answer": "replace()"},
    {"question": "What does the split() function do?", "options": ["Joins strings", "Splits a string into a list", "Removes spaces", "Counts words"], "answer": "Splits a string into a list"},
    {"question": "Which escape character represents a newline?", "options": ["\\n", "\\t", "\\r", "\\b"], "answer": "\\n"},
    {"question": "Which method checks if a string starts with a specific substring?", "options": ["startswith()", "endswith()", "contains()", "find()"], "answer": "startswith()"},
    {"question": "Which method returns a string with leading zeros?", "options": ["zfill()", "pad()", "fill()", "zeros()"], "answer": "zfill()"},
    {"question": "What will 'python'.capitalize() return?", "options": ["PYTHON", "Python", "python", "P"], "answer": "Python"},
    {"question": "Which function checks the data type of a variable?", "options": ["type()", "isinstance()", "dtype()", "typeof()"], "answer": "type()"},
    {"question": "Which method is used to check if all characters in a string are alphabets?", "options": ["isalpha()", "isdigit()", "isalnum()", "isletter()"], "answer": "isalpha()"},
    {"question": "How do you format a string using placeholders?", "options": ["format()", "replace()", "insert()", "concat()"], "answer": "format()"}
],

 "Control Flow (Loops & Conditions)": [
    {"question": "Which statement is used for decision making?", "options": ["if", "for", "while", "switch"], "answer": "if"},
    {"question": "Which loop is used when the number of iterations is known?", "options": ["for", "while", "do-while", "None"], "answer": "for"},
    {"question": "Which keyword is used to exit a loop prematurely?", "options": ["exit", "stop", "break", "end"], "answer": "break"},
    {"question": "Which keyword is used to skip an iteration in a loop?", "options": ["skip", "continue", "break", "pass"], "answer": "continue"},
    {"question": "What does the 'else' block in a loop do?", "options": ["Executes after loop ends normally", "Runs before loop starts", "Runs only if condition is False", "Causes an error"], "answer": "Executes after loop ends normally"},
    {"question": "Which loop will execute at least once, even if the condition is false?", "options": ["for", "while", "do-while", "None"], "answer": "do-while"},
    {"question": "What is the correct syntax for a for loop in Python?", "options": ["for i in range(5):", "for (i=0; i<5; i++)", "foreach i in range(5)", "loop i in range(5)"], "answer": "for i in range(5):"},
    {"question": "Which statement is used to check multiple conditions?", "options": ["if", "if-elif-else", "switch", "while"], "answer": "if-elif-else"},
    {"question": "What will `while True:` do?", "options": ["Run forever", "Run once", "Run if True", "Cause an error"], "answer": "Run forever"},
    {"question": "Which loop is best when the number of iterations is unknown?", "options": ["for", "while", "do-while", "None"], "answer": "while"},
    {"question": "What does the pass statement do?", "options": ["Skips execution but avoids an error", "Exits the loop", "Skips the next iteration", "Does nothing"], "answer": "Skips execution but avoids an error"},
    {"question": "Which keyword is used for a conditional expression?", "options": ["switch", "elif", "else", "ternary"], "answer": "elif"},
    {"question": "How do you check if two values are equal?", "options": ["=", "==", "!=", "equals()"], "answer": "=="},
    {"question": "Which operator is used for logical AND?", "options": ["&", "&&", "and", "|"], "answer": "and"},
    {"question": "Which operator is used for logical OR?", "options": ["|", "||", "or", "&"], "answer": "or"},
    {"question": "Which statement is used for looping over a list?", "options": ["for", "while", "do-while", "loop"], "answer": "for"},
    {"question": "Which loop will not run if the condition is False initially?", "options": ["for", "while", "do-while", "None"], "answer": "while"},
    {"question": "How do you reverse iterate through a range?", "options": ["for i in range(5, 0, -1)", "for i in reverse(5)", "for i in range(0,5,-1)", "for i in range(5,-1,0)"], "answer": "for i in range(5, 0, -1)"},
    {"question": "Which statement is used to exit multiple nested loops at once?", "options": ["break", "continue", "exit", "return"], "answer": "break"},
    {"question": "Which keyword is used to define a condition?", "options": ["if", "else", "elif", "while"], "answer": "if"}
],

"Lists, Tuples & Dictionaries": [
    {"question": "Which data type is mutable?", "options": ["Tuple", "String", "List", "Integer"], "answer": "List"},
    {"question": "How do you access the first element of a list?", "options": ["list[0]", "list[1]", "list.get(0)", "first(list)"], "answer": "list[0]"},
    {"question": "Which method adds an element to the end of a list?", "options": ["add()", "insert()", "append()", "extend()"], "answer": "append()"},
    {"question": "How do you remove a key-value pair from a dictionary?", "options": ["del dict[key]", "remove dict[key]", "pop(dict[key])", "discard dict[key]"], "answer": "del dict[key]"},
    {"question": "Which data structure uses key-value pairs?", "options": ["List", "Set", "Tuple", "Dictionary"], "answer": "Dictionary"},
    {"question": "Which method returns the number of elements in a list?", "options": ["size()", "count()", "len()", "length()"], "answer": "len()"},
    {"question": "How do you add multiple elements to a list at once?", "options": ["append()", "insert()", "extend()", "addAll()"], "answer": "extend()"},
    {"question": "What will `my_tuple = (1, 2, 3); my_tuple[1] = 5` do?", "options": ["Update tuple", "Add a new element", "Raise an error", "Replace whole tuple"], "answer": "Raise an error"},
    {"question": "How do you get all the keys from a dictionary?", "options": ["dict.keys()", "dict.values()", "dict.items()", "get_keys(dict)"], "answer": "dict.keys()"},
    {"question": "Which of the following is **immutable**?", "options": ["List", "Dictionary", "Tuple", "Set"], "answer": "Tuple"},
    {"question": "Which method removes and returns the last element of a list?", "options": ["remove()", "delete()", "pop()", "discard()"], "answer": "pop()"},
    {"question": "Which method sorts a list in-place?", "options": ["sort()", "sorted()", "order()", "arrange()"], "answer": "sort()"},
    {"question": "Which method creates a shallow copy of a list?", "options": ["copy()", "duplicate()", "clone()", "copy_list()"], "answer": "copy()"},
    {"question": "How do you check if a key exists in a dictionary?", "options": ["key in dict", "dict.has_key(key)", "exists(dict, key)", "contains(dict, key)"], "answer": "key in dict"},
    {"question": "Which method is used to get a value from a dictionary safely?", "options": ["dict.value()", "dict.get()", "dict.fetch()", "dict.retrieve()"], "answer": "dict.get()"},
    {"question": "What will `len({1: 'a', 2: 'b', 3: 'c'})` return?", "options": ["3", "6", "2", "Error"], "answer": "3"},
    {"question": "Which method removes a specific item from a list?", "options": ["remove()", "delete()", "pop()", "discard()"], "answer": "remove()"},
    {"question": "Which of the following can store duplicate values?", "options": ["List", "Dictionary", "Set", "None"], "answer": "List"},
    {"question": "Which method returns key-value pairs from a dictionary?", "options": ["dict.keys()", "dict.values()", "dict.items()", "dict.pairs()"], "answer": "dict.items()"}
],

}
# Sidebar - Chapter Selection
selected_chapter = st.sidebar.radio("📚 Select a Chapter", list(quiz_data.keys()))
questions = quiz_data[selected_chapter]

# Session State Initialization
if "index" not in st.session_state or st.session_state.selected_chapter != selected_chapter:
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.selected_chapter = selected_chapter
    st.session_state.questions = random.sample(questions, len(questions))  # Shuffle questions
    st.session_state.answered = False
    st.session_state.user_answers = []  # Store user answers

# Progress Indicator
st.progress(st.session_state.index / len(st.session_state.questions))
st.write(f"📌 **Question {st.session_state.index + 1} of {len(st.session_state.questions)}**")

# Get Current Question
if st.session_state.index < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.index]
    st.subheader(q["question"])
    
    selected_option = st.radio("Choose your answer", q["options"], key=f"answer_{st.session_state.index}")

    # Buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Submit", disabled=st.session_state.answered):
            st.session_state.user_answers.append({"question": q["question"], "selected": selected_option, "correct": q["answer"]})
            if selected_option == q["answer"]:
                st.success("✅ Correct Answer!")
                st.session_state.score += 1
            else:
                st.error(f"❌ Incorrect! The correct answer is {q['answer']}")
            st.session_state.answered = True  

    with col2:
        if st.button("Next"):
            st.session_state.index += 1
            st.session_state.answered = False  
            st.rerun()

# Show Final Result
else:
    st.success(f"🎉 Quiz Completed! Chapter: **{st.session_state.selected_chapter}**")
    st.write(f"✅ **Your Score: {st.session_state.score}/{len(st.session_state.questions)}**")
    
    st.subheader("📊 Detailed Report")
    for ans in st.session_state.user_answers:
        if ans["selected"] == ans["correct"]:
            st.write(f"✅ **{ans['question']}** - Your Answer: **{ans['selected']}** (Correct)")
        else:
            st.write(f"❌ **{ans['question']}** - Your Answer: **{ans['selected']}** | Correct Answer: **{ans['correct']}**")
    
    if st.button("Restart Quiz 🔄"):
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.questions = random.sample(questions, len(questions))
        st.session_state.answered = False
        st.session_state.user_answers = []
        st.rerun()