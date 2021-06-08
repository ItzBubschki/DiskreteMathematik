from prettytable import PrettyTable

base = int(input("Enter base num: "))
mod_base = int(input("Enter the mod base: "))

def calculate_row(first, second):
    value = [first, second]
    value.append(first%second)
    value.append(int(first/second))
    return value

def calculate_second_num(prev_row, current_row):
    return prev_row[4] - current_row[3] * current_row[4]

current_row = calculate_row(base, mod_base)
rows = [current_row]
while current_row[2] != 0:
    last_row = rows[len(rows)-1]
    current_row = calculate_row(last_row[1], last_row[2])
    rows.append(current_row)

for i in range(len(rows)-1, -1, -1):
    if i == len(rows)-1:
        rows[i].append(0)
        rows[i].append(1)
    else:
        rows[i].append(rows[i+1][5])
        rows[i].append(calculate_second_num(rows[i+1], rows[i]))

t = PrettyTable(['a', 'b', 'r', 'q', 'x', 'y'])
for i in rows:
    t.add_row(i)
print(t)
print(f"The final result is {rows[0][4]%mod_base}")