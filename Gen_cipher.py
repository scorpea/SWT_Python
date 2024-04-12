import random
import string

# Function to generate a random cipher text of length 3
def generate_cipher_text():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(3))

# Generate 300 cipher texts and join them on a single line
cipher_texts = [generate_cipher_text() for _ in range(300)]
cipher_text_line = ''.join(cipher_texts)

# Print the single line with 300 cipher texts
print(cipher_text_line)
