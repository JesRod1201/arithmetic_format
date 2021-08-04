def arithmetic_arranger(problems, con = False):
  #inputs(5)
  if len(problems) > 5 :
    return('Error: Too many problems.')

  #lists
  foper = list()
  soper = list()
  opera = list()
  res = list()
  fline = str()
  sline = str()
  tline = str()
  aline = str()

  #split section
  for problem in problems:
    problem.lstrip()
    problem.rstrip()
    sproblem = problem.split(" ")
    if len(sproblem[0]) > 4 or len(sproblem[2]) > 4:
      return('Error: Numbers cannot be more than four digits.')
    if not (sproblem[1] == '+' or sproblem[1] == '-'):
      return('Error: Operator must be \'+\' or \'-\'.')
    foper.append(sproblem[0])
    opera.append(sproblem[1])
    soper.append(sproblem[2])

  #arithmetic
  counter = 0
  while counter < len(problems):
    try:
      a = int(foper[counter])
      b = int(soper[counter])
    except:
      return('Error: Numbers must only contain digits.')
    if opera[counter] == '+':
      res.append(str(a + b))
    elif opera[counter] == '-':
      res.append(str(a - b))

    #find widht
    long = max(len(foper[counter]), len(soper[counter]))

    #1st line
    for val in range((long + 2) - len(foper[counter])):
      foper[counter] = ' ' + foper[counter]
    fline = fline + foper[counter] + '    '

    #2nd line
    for val in range((long + 1)- len(soper[counter])):
      soper[counter] = ' ' + soper[counter]
    sline = sline + opera[counter] + soper[counter] + '    '

    #3rd line
    for val in range(long + 2):
      tline = tline + '-'
    tline = tline + '    '

    #4th line
    for val in range((long + 2) - len(res[counter])):
      res[counter] = ' ' + res[counter]
    aline = aline + res[counter] + '    '

    counter = counter + 1

  #Final output
  fline = fline.rstrip()
  sline = sline.rstrip()
  tline = tline.rstrip()
  aline = aline.rstrip()
  if con == False:
    arranged_problems = fline + '\n' + sline + '\n' + tline
  elif con == True:
    arranged_problems = fline + '\n' + sline + '\n' + tline + '\n' + aline

  return arranged_problems
