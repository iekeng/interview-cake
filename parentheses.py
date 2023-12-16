def parentheses_validator(s):
    stack = []
    openers = ['{', '[', '(']
    closers = {'}': '{', ']': '[', ')': '('}

    for char in s:
        if char in openers:
            stack.append(char)
        elif char in closers:
            if not stack or stack.pop() != closers[char]:
                return False
    return not stack
