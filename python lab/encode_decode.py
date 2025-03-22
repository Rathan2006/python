def decode_message(encoded_message):
    def helper(s, memo):
        if s in memo:
            return memo[s]
        if not s:
            return ['']
        
        result = []
        
        for i in range(1, 3):
            if i <= len(s):
                number = int(s[:i])
                if 1 <= number <= 26:
                    for sub in helper(s[i:], memo):
                        result.append(chr(number + 64) + sub)
        
        memo[s] = result
        return result

    return helper(encoded_message, {})

def main():
    encoded_message = input("Enter encoded message: ")
    decoded_messages = decode_message(encoded_message)
    print("Possible decoded messages:")
    for message in decoded_messages:
        print(message)

if __name__ == "__main__":
    main()
