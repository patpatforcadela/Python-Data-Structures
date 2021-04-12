from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

    def top(self):
        return self.stack[-1]

    def printStack(self):
        for item in range(self.size()-1, -1, -1):
            print(" | " + str(self.stack[item]) + " | ")
        print("  ---")

def reverse_string(string):
    temp_st = Stack()
    for letter in string:
        temp_st.push(letter)
    for _ in range(len(string)):
        print(temp_st.pop(), end="")

def isBalanced(string):
    temp_st = Stack()
    balance = True
    for letter in string:
        if letter == '(' or letter == '{' or letter == '[':
            temp_st.push(letter)
        if temp_st.isEmpty() and (letter == ')' or letter == '}' or letter == ']'):
            return False
        if (letter == ')' and temp_st.top() == '(') or (letter == '}' and temp_st.top() == '{') or (letter == ']' and temp_st.top() == '['):
            temp_st.pop()

    return True if temp_st.isEmpty() else False

st = Stack()
st.push(3)
st.push(5)
st.push(7)
st.push(9)
print(isBalanced("[a+b]*(x+2y)*{gg+kk}"))

