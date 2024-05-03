def mark_brackets(string):
    
    n = len(string)
    right_pos = []
    left_pos = []
    ans = []
    stack = []
    
    for i in range(n):
        if string[i] != '(' and string[i] != ')':
            continue
        elif string[i] == ')' and not stack:
            right_pos.append(i)
        elif string[i] == ')' and stack:
            stack.pop()
        elif string[i] == '(':
            stack.append(i)
            
    left_pos = stack
    
    for i in range(n):
        if i in left_pos:
            ans.append('x')
        elif i in right_pos:
            ans.append('?')
        else:
            ans.append(' ')
            
    return "".join(ans)
    
# Test cases
print(mark_brackets("bge)))))))))"))   
print(mark_brackets("((IIII))))))"))   
print(mark_brackets("()()()()(uuu"))   
print(mark_brackets("))))UUUU((()"))   