def data_printer(c):
  
  # Section 1: Makes a list for each column where the first entry is the column_name
  #            and the following entries are the data per column.
  columns = [[line[0]] for line in c.description] # See EXTRA 1 and/or 1.5 for more info
  for data in c.fetchall():
    for num in range(len(columns)):
      columns[num].append(str(data[num]))
  
  # Section 2: The maximum character length, inside a column, per column is stored in a
  #            list. This is used to determine how many spaces should be added to a word
  #            to keep the column_width consistent.
  lengths = []
  for num in range(len(columns)):
    lengths.append(max([len(entry) for entry in columns[num]]))
  
  # Section 3: A dict is made where the value of each key holds the data per row in a list.
  #            A striped line of the max. length per column is added to the second row.
  #            When the data can be converted into an int, the spaces are added to the left
  #            otherwise spaces are added to the right.
  output = {}
  for col in range(len(columns)):
    columns[col].insert(1, "-" * lengths[col])
    for row in range(len(columns[col])):

      if not row in output:
        output[row] = []
      try:
        test = int(columns[col][row])
        output[row].append(" " * (lengths[col] - len(columns[col][row])) + columns[col][row])
      except ValueError:
        output[row].append(columns[col][row] + " " * (lengths[col] - len(columns[col][row])))
  
  print("\n")
  [print("  ".join(output[row])) for row in range(len(output.keys()))]
  print("\n")