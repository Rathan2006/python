import re

def tokenize(text):
    # Regular expressions for different tokens
    patterns = {
        'date': r'\d{1,2}/\d{1,2}/\d{2,4}|\d{1,2}-\d{1,2}-\d{2,4}',
        'url': r'https?://[^\s]+',
        'email': r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
        'number': r'\d+(\.\d+)?|\d{1,3}(,\d{3})*(\.\d+)?',
        'username': r'@[a-zA-Z0-9_]+',
        'punctuation': r'[!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]',
    }

    # Combining the patterns into a single regular expression
    combined_pattern = '|'.join(f'(?P<{key}>{pattern})' for key, pattern in patterns.items())

    # Tokenizing the text
    tokens = []
    for match in re.finditer(combined_pattern, text):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        tokens.append((token_type, token_value))

    return tokens

def main():
    text = input("Enter text to tokenize: ")
    tokens = tokenize(text)
    print("Tokens:")
    for token_type, token_value in tokens:
        print(f"{token_type}: {token_value}")

if __name__ == "__main__":
    main()
