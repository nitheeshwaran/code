file_location = r"C:\Users\NITHEESH\OneDrive\Desktop\sample_input.txt"
output_locaton = r"C:\Users\NITHEESH\OneDrive\Desktop\output.txt"

file1 = open(file_location, 'r')
Lines = file1.readlines()
M = int(Lines[0].replace("Number of employees: ", "")) - 1
d = dict()
for i in Lines[4:]:
    k = i.split(': ')
    d[int(k[1])] = k[0]
n = len(d)

k = list(d.keys())
k.sort()
final = []
for i in range(n - M):
    final.append(k[i + M] - k[i])

kk = 0
mn = final[0]
for i in range(1, n - M):
    if (mn > final[i]):
        mn = final[i]
        kk = i

ans = "The goodies selected for distribution are:\n\n"

for i in k[kk:kk + M + 1]:
    ans += d[i] + ": " + str(i) + "\n"
ans += "\nAnd the difference between the chosen goodie with highest price and the lowest price is " + str(mn)

print(ans)

# Writing output

file1 = open(output_locaton, 'w')
file1.write(ans)
file1.close()
