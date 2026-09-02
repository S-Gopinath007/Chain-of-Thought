INPUT_FILE = "mock_data.log"
OUTPUT_FILE = "filtered_errors.txt"

try:
    with open(INPUT_FILE, 'r', encoding='utf-8') as infile:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
            for line in infile:
                if line.startswith('CRITICAL') or line.startswith('FATAL'):
                    outfile.write(line)
except FileNotFoundError:
    print(f"Error: {INPUT_FILE} not found.")