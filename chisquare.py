tabulated_val = float(input("Enter the tabulated chi-square value: "))
m = int(input("Enter number of rows: "))

print("Enter data for each row:")
observed = []

for i in range(m):
    row = [float(x) for x in input(f"Row {i+1}: ").replace(",", " ").split()]
    observed.append(row)

rows = m
cols = len(observed[0])

row_totals = [sum(row) for row in observed]
col_totals = [sum(observed[r][c] for r in range(rows)) for c in range(cols)]
grand_total = sum(row_totals)

print("\n" + "-" * 55)
print("Row\tCol\tObserved(O)\tExpected(E)\t(O-E)^2/E")
print("\n" + "-" * 55)

chi_square_stat = 0

for r in range(rows):
    for c in range(cols):
        o_val = observed[r][c]
        e_val = (row_totals[r] * col_totals[c]) / grand_total
        cell_chi = ((o_val - e_val) ** 2) / e_val
        chi_square_stat += cell_chi

        print(f"{r+1}\t{c+1}\t{o_val:.2f}\t\t{e_val:.4f}\t\t{cell_chi:.4f}")

print("\n" + "-" * 55)

df = (rows - 1) * (cols - 1)

print("\n---Summary---")
print(f"Degree of Freedom (df) = {df}")
print(f"Calculated Chi-square value = {chi_square_stat:.4f}")
print(f"Tabulated Chi-square value = {tabulated_val:.4f}")

if chi_square_stat < tabulated_val:
    print("\nDecision: Accept the Null Hypothesis (H0)")
else:
    print("\nDecision: Reject the Null Hypothesis (H0)")