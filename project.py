import random

# Step 1: Generate random bits
def generate_bits(n):
    return [random.randint(0,1) for i in range(n)]

# Step 2: Generate random bases (+ or x)
def generate_bases(n):
    bases = []
    for i in range(n):
        bases.append(random.choice(['+', 'x']))
    return bases

# Step 3: Bob measures qubits
def measure_bits(alice_bits, alice_bases, bob_bases):
    results = []
    
    for i in range(len(alice_bits)):
        if alice_bases[i] == bob_bases[i]:
            results.append(alice_bits[i])
        else:
            results.append(random.randint(0,1))
            
    return results

# Step 4: Generate shared key
def generate_key(alice_bits, alice_bases, bob_bases, bob_results):
    
    alice_key = []
    bob_key = []
    
    for i in range(len(alice_bits)):
        if alice_bases[i] == bob_bases[i]:
            alice_key.append(alice_bits[i])
            bob_key.append(bob_results[i])
            
    return alice_key, bob_key


# Step 5: Encrypt message using key
def encrypt(message, key):
    
    binary_msg = ''.join(format(ord(i),'08b') for i in message)
    
    encrypted = ""
    
    for i in range(len(binary_msg)):
        encrypted += str(int(binary_msg[i]) ^ key[i % len(key)])
        
    return encrypted


# Step 6: Decrypt message
def decrypt(cipher, key):
    
    decrypted = ""
    
    for i in range(len(cipher)):
        decrypted += str(int(cipher[i]) ^ key[i % len(key)])
    
    chars = [decrypted[i:i+8] for i in range(0,len(decrypted),8)]
    
    message = ""
    
    for c in chars:
        message += chr(int(c,2))
        
    return message


# MAIN PROGRAM

n = 50

alice_bits = generate_bits(n)
alice_bases = generate_bases(n)

bob_bases = generate_bases(n)

bob_results = measure_bits(alice_bits, alice_bases, bob_bases)

alice_key, bob_key = generate_key(alice_bits, alice_bases, bob_bases, bob_results)

print("Shared Secret Key:", alice_key)

message = input("Enter message to send securely: ")

cipher = encrypt(message, alice_key)

print("Encrypted Message:", cipher)

decrypted = decrypt(cipher, bob_key)

print("Decrypted Message:", decrypted)