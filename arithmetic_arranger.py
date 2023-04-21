def arithmetic_arranger(operation):
  a = list()
  b = list()
  if len(operation) > 5:
    return "Error: Too many problems."
  for op in operation:
    a.append(op.split())
    e = op.split()
    max_len = len(max(e, key=len))
    line_len = max_len + 2
    x = len(a)
    for i in range(x):
      if a[i][0].isnumeric() and a[i][2].isnumeric():
        max_len = len(max(op.split(), key=len))
        if max_len <= 4:
          if a[i][1] == '+':
            c = int(a[i][0]) + int(a[i][2])
          elif a[i][1] == '-':
            c = int(a[i][0]) - int(a[i][2])
          else:
            return "Error: Operator must be '+' or '-'."
        else:
          return "Error: Numbers cannot be more than four digits."
      else:
        return "Error: Numbers must only contain digits."
    b.append(c)
  line = '-' * line_len
  top = []
  bottom = []
  lines = []
  result = []
  for i in range(x):
    top.append(a[i][0].rjust(line_len, ' '))
    bottom.append(f"{a[i][1]}{' '*(line_len-len(a[i][2])-1)}{a[i][2]}")
    lines.append(line)
    result.append(f"{' '*(line_len-max(len(a[i][0]),len(a[i][2])))}{b[i]}")
    ab = '\n'.join(['   '.join(i) for i in (top, bottom, lines, result)])
  print(ab)
