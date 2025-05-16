print("\t ............MULTIPLICATION TABLE...........")
print("    ", end="")
for i in range(1, 10):
    print(f"{i:4}", end="")
print("\n" + "-" * 40)

for i in range(1, 10):
    print(f"{i:2} |", end="")
    for j in range(1, 10):
        print(f"{i * j:4}", end="")
    print()
