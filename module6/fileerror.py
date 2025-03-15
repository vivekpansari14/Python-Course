import time
import sys

code = """with open("example.txt", "w") as file:
    file.write("Hello, VKPXR Fam! This is your first automated file.")"""

for char in code:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)  # Adjust speed for effect

print("\n\n✅ File created successfully!")  
