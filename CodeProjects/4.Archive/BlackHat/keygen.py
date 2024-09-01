from Crypto.PublicKey import RSA

new_key = RSA.generate(2048)

public_key = new_key.public().exportkey("PEM")
private_key = new_key.exportKey("PEM")

print(f"Public key: {public_key}")
print()
print(f"Private key:{private_key}")