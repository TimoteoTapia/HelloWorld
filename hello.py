def dynamic_hello(name=None):
    if name:
        return f"Hello, {name}!\nHello, World!"
    else:
        return "Hello, World!"

# Ejecución
if __name__ == "__main__":
    user_input = input("Enter your name (or press Enter for default): ")
    print(dynamic_hello(user_input.strip()))
