# Sensor Log Combiner and Timestamp Formatter

This repository provides a lightweight C and Python toolchain for combining and formatting sensor or log data stored in `.txt` files. It's ideal for preprocessing time-series data collected from embedded systems or sensor devices before analysis or visualization.

---

## 🗂 Project Structure

- **combine_text_file.c**  
  A C program that scans a directory, finds `.TXT` or `.txt` files, reorders them based on filename patterns, and merges them into a single output file.

- **file_testing.py**  
  A Python script that modifies the first field (e.g., timestamp) in each line of the combined file using a custom numerical time increment format.

- **file_testing_modify.py**  
  An enhanced Python script that reformats the timestamp into a structured, human-readable format (`dd,hh:mm:ss`) while preserving sensor values.

---

## 🛠 How to Use

### 1. **Combine Files**
Compile and run the C program to combine `.txt` files from a directory.

```bash
gcc combine_text_file.c -o combine
./combine
```
Edit the hardcoded path[] in the source file to your actual folder path.

2. Format Timestamps
After generating the combined file, run either of the following:

➤ Basic Time Increment
```bash
python file_testing.py
```

➤ Human-Readable Format
```bash
python file_testing_modify.py
```
Both scripts will ask for a numeric start time (e.g., hhmmss) and generate a modified .txt output.

📂 Example Output
Before

```bash
time=3000000, sensor1=12, sensor2=25,...
```
After (file_testing_modify.py)

```bash
30,00:00:01,12,25,...
```
🔧 Requirements
C compiler (e.g., GCC)

Python 3.x

📌 Notes
File ordering is based on specific characters in filenames (e.g., xxxx000.txt, xxxx001.txt, etc.).

You can adjust the formatting logic to match your sensor data format.
