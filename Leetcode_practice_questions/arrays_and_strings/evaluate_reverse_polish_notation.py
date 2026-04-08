#https://leetcode.com/problems/evaluate-reverse-polish-notation/?envType=study-plan-v2&envId=top-interview-150

class Solution :
  def evalRPN( self, tokens: list[str]):
    stack = []
    for token in tokens:
      if token not in '-+/*':
        stack.append(int(token))
      else:
        second = stack.pop()
        first = stack.pop()
        if token == '+':
          stack.append(first+second)
        elif token == '-':
          stack.append(first-second)
        elif token == '*':
          stack.append(first*second)
        elif token == '/':
          stack.append(first/second)
      return stack[0]
