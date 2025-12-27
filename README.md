# Text-Analyzer
📝 Text Analyzer (Python)

A Python-based Text Analyzer that processes a word or sentence entered by the user and provides:

Total number of letters

Total number of numbers

List of repeated letters (case-insensitive)

This project is designed for beginners to practice string manipulation, loops, and dictionaries in Python.

🚀 Features

📥 Accepts a word or full sentence as input

🔤 Counts total alphabetic characters

🔢 Counts total numeric digits

🔁 Identifies repeated letters

🔡 Case-insensitive analysis

🧑‍🎓 Easy-to-understand logic

🛠️ Technologies Used

Python 3

String methods: isalpha(), isdigit(), lower()

Dictionary for frequency counting

Loops and conditional statements

📂 Project Structure
Text-Analyzer/
│
├── text_analyzer.py   # Main Python script
└── README.md          # Project documentation

▶️ How to Run the Program
1️⃣ Clone the Repository
git clone https://github.com/your-username/Text-Analyzer.git

2️⃣ Navigate to the Project Folder
cd Text-Analyzer

3️⃣ Run the Program
python text_analyzer.py

🧪 Example
Input
Enter words or a sentence: Hello World 123

Output
Total letters: 10
Total numbers: 3

Repeated letters:
l = 3
o = 2

📄 Source Code
text = input("Enter words or a sentence: ")

letters = 0
numbers = 0
letter_count = {}

for char in text:
    if char.isalpha():
        letters += 1
        char = char.lower()
        letter_count[char] = letter_count.get(char, 0) + 1
    elif char.isdigit():
        numbers += 1

print("Total letters:", letters)
print("Total numbers:", numbers)

print("\nRepeated letters:")
for letter, count in letter_count.items():
    if count > 1:
        print(letter, "=", count)

🧠 How It Works

isalpha() → checks if a character is a letter

isdigit() → checks if a character is a digit

Dictionary stores the frequency of each letter

Only letters with count > 1 are displayed

📚 Learning Outcomes

This project helps you learn:

String traversal

Character classification

Dictionary-based counting

Case-insensitive text processing

Basic text analysis logic

🚀 Future Enhancements

Count vowels and consonants

Display most frequent character

Ignore special symbols and spaces

Analyze text from a file

Create a GUI using Tkinter

👨‍💻 Author

Syam Sundar
📍 India
💡 Python | Java | Programming Enthusiast

📄 License

This project is open-source and free to use for educational purposes.
