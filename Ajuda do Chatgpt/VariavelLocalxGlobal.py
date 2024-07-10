# Variável global
x = 10

# Uma função é invocada através do def
def print_number():
    # Variável local
    x = 5
    print(f"Local x: {x}")  # Output: Local x: 5

print_number()
print(f"Global x: {x}")  # Output: Global x: 10
