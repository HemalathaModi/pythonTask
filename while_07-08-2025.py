class_no = 1
n = 10
m = 30
while class_no <= n:
  roll_no = 1
  if class_no % 3 == 0:
    continue
  while roll_no <= m:
    if roll_no > 15:
      break
    print(f'Class{class_no} Roll{roll_no}')
    roll_no += 1
  roll_no += 1
