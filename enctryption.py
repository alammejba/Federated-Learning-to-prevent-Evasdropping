import base64

def longest_substring(str,l):
	x = []
	n = len(str)
	ans = 0
	for i in range(n):
		for j in range(i+1, n):
			if str[i] == str[j] and len(str[i:j+1])==l:
				ans = str[i:j+1]
				x.append(ans)
	return x


def base64_encode(string):
    # Convert string to bytes
    message_bytes = string.encode('utf-8')
    
    # Use base64 library to encode bytes
    base64_bytes = base64.b64encode(message_bytes)
    
    # Decode bytes to string
    return base64_bytes.decode('utf-8')

def base64_decode(encoded_string):
    # Convert encoded string to bytes
    encoded_bytes = encoded_string.encode('utf-8')
    
    # Use base64 library to decode bytes
    decoded_bytes = base64.b64decode(encoded_bytes)
    
    # Decode bytes to string
    return decoded_bytes.decode('utf-8')


# message = "demo"
# encoded_message = base64_encode(message)
# print("encoded message: ",encoded_message)

# decoded_message = base64_decode(encoded_message)
# print("encoded message: ",decoded_message)


str = 'phiBaPk25mis/PNyepPD4TkFAixMMI4Hi0gvFiOzqYYZGVtbw==Y93ltkqDbbw9WTqH4EQiXaB7WVIWGd/DgKTFwTey5Tg61vTEmNO+ckkjX9zua6UAQMieHLKmpoXOpKTARFIMb17jkFYASjeHWsxFgLXlga4wROsKbhPQvs+pqMaOSVGsxo='

print(longest_substring(str,10))