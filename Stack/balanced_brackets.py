#
# Determnine whether a given sequence of brackets is balanced
# HackerRank
#

def is_balanced(s):

    stack = []
    for b in s:

        # Push closing bracket onto stack when opening bracket is read
        # Then if reading a closing braket, can check stack top for itself
        if (b=='{'):
            stack.append('}')
        elif (b=='['):
            stack.append(']')
        elif (b=='('):
            stack.append(')')
        else:
            if (len(stack)==0 or stack[-1]!=b):
                return False

            stack.pop()

    return len(stack)==0


# Demonstration
def main():

    s = "[[{()}]]"
    print(s)
    print(is_balanced(s))

main()
