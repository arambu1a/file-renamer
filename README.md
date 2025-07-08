# File Renamer 

This simple Python script renames all text files in a folder by appending the current date to the filenames. It's a small but useful project inspired from Day 1 of the "100 Days of Code: Python Bootcamp".

## 📁 How It Works

- Looks inside the `files` folder
- Reads each `.txt` file
- Gets the current date (`YYYY-MM-DD`)
- Renames each file by appending the date to its name
  - Example: `a.txt` ➡️ `a-2025-07-08.txt`

## 🧠 Concepts Used

- Python's `os` module
- File handling (`open`, `read`)
- String manipulation
- `datetime` for formatting dates

## 🚀 How to Use

1. Put your `.txt` files inside a folder named `files` (in the same directory as the script).
2. Run the script
