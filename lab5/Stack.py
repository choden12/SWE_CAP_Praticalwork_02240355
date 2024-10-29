class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)

# Test the Stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Should print 3
print(stack.peek())  # Should print 2
print(stack.size())  # Should print 2

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)

# Test the Queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Should print 1
print(queue.front())  # Should print 2
print(queue.size())  # Should print 2

def is_balanced(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty():
                return False
            stack.pop()
    return stack.is_empty()

# Test the function
print(is_balanced("((()))"))  # Should print True
print(is_balanced("(()"))  # Should print False

def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"

def reverse_string(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Test the function
print(reverse_string("Hello, World!"))  # Should print "!dlroW ,olleH"


def hot_potato(names, num):
    queue = Queue()
    for name in names:
        queue.enqueue(name)
    
    while queue.size() > 1:
        for _ in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()

# Test the function
names = ["Pika", "Sangay", "Beam", "Sonam", "Yeshey", "Tenzin"]
print(hot_potato(names, 7))  # The winner's name will be printed


print("/nExercise1")

def evaluate_postfix(expression):
    stack = []  # Initialize an empty stack
    
    # Iterate through each token in the expression
    for token in expression:
        if token.isdigit():  # If token is an operand, push it to the stack
            stack.append(int(token))
        else:
            # Pop the last two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            # Apply the operator
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2  
            
            # Push the result back onto the stack
            stack.append(result)
    
    # The final result should be the only element in the stack
    return stack.pop()

# Test the function
postfix_expression = "231*+9-"
print("Postfix Expression:", postfix_expression)
result = evaluate_postfix(postfix_expression)
print("Evaluated Result:", result)

print("/nExercise2")

class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # Stack for enqueue operations
        self.stack2 = []  # Stack for dequeue operations

    def enqueue(self, item):
        # Push the item onto stack1
        self.stack1.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        # If both stacks are empty, raise an error
        if not self.stack1 and not self.stack2:
            raise IndexError("Dequeue from an empty queue")
        
        # If stack2 is empty, transfer all items from stack1 to stack2
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        # Pop the item from stack2, which is the front of the queue
        return self.stack2.pop()

# Test the QueueUsingStacks class
queue = QueueUsingStacks()

# Enqueue some items
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# Dequeue items and print them
print("Dequeued:", queue.dequeue())  # Should print 1
print("Dequeued:", queue.dequeue())  # Should print 2

# Enqueue another item
queue.enqueue(4)

# Dequeue the remaining items
print("Dequeued:", queue.dequeue())  # Should print 3
print("Dequeued:", queue.dequeue())  # Should print 4

print("/nExercise3")

from collections import deque
import time

class TaskScheduler:
    def __init__(self):
        self.task_queue = deque()  # Initialize an empty queue for tasks

    def add_task(self, task, description="Task"):
        """Adds a task to the queue."""
        self.task_queue.append((task, description))
        print(f"Added: {description}")

    def run_tasks(self):
        """Processes each task in the order it was added."""
        while self.task_queue:
            task, description = self.task_queue.popleft()  # Get the next task
            print(f"Processing: {description}")
            task()  # Execute the task
            print(f"Completed: {description}\n")
            time.sleep(1)  # Simulate a delay between tasks

# Example tasks
def task1():
    print("Running Task 1...")

def task2():
    print("Running Task 2...")

def task3():
    print("Running Task 3...")

# Create an instance of TaskScheduler
scheduler = TaskScheduler()

# Add tasks to the scheduler
scheduler.add_task(task1, "Task 1")
scheduler.add_task(task2, "Task 2")
scheduler.add_task(task3, "Task 3")

# Run all tasks
scheduler.run_tasks()


print("Exercise4")

# Define precedence and associativity
precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
associativity = {'+': 'L', '-': 'L', '*': 'L', '/': 'L'}

def infix_to_postfix(expression):
    output = []  # Output list to hold the postfix expression
    stack = []   # Stack to hold operators

    for token in expression:
        if token.isalnum():  # If the token is an operand (alphanumeric), add it to output
            output.append(token)
        elif token == '(':  # If the token is '(', push it to the stack
            stack.append(token)
        elif token == ')':  # If the token is ')', pop until '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Pop the '(' from the stack
        else:
            # Pop operators from the stack to output if they have higher or equal precedence
            while (stack and stack[-1] != '(' and
                   (precedence[stack[-1]] > precedence[token] or
                    (precedence[stack[-1]] == precedence[token] and associativity[token] == 'L'))):
                output.append(stack.pop())
            stack.append(token)  # Push the current operator onto the stack

    # Pop any remaining operators in the stack
    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Test the function
expression = "A+B*C-(D/E+F*G)*H"
print("Infix Expression:", expression)
postfix_expression = infix_to_postfix(expression)
print("Postfix Expression:", postfix_expression)
