submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice","Frank"]

print('Alice' in submitted)
print('Alice' in attended)

if 'Alice' in submitted and attended:
    print(True)
else:
    print(False)