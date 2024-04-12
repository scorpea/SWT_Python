# Function to calculate the number of days needed to transform the cipher text
def transform_to_per(cipher_text):
    target = "PER" * (len(cipher_text) // 3)
    days = 0

    while cipher_text != target:
        for i in range(len(cipher_text)):
            if cipher_text[i] != target[i]:
                cipher_text = cipher_text[:i] + target[i] + cipher_text[i + 1:]
                days += 1
                break

    return days


# Read input from stdin.txt
with open("stdin.txt", "r") as input_file:
    cipher_text = input_file.readline().strip()

# Convert to uppercase for case-insensitivity
cipher_text = cipher_text.upper()

# Calculate the number of days needed
days_needed = transform_to_per(cipher_text)

# Write the result to stdout.txt
with open("stdout.txt", "w") as output_file:
    output_file.write(str(days_needed))
