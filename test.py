char = 'a'
hex_char = char.encode("hex")
print hex_char
hex_char++
print hex_char
char = hex_char.decode("hex")
print char