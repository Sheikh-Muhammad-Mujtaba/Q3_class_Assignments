# 📚 Personal Library Manager

## Overview
The **Personal Library Manager** is a **Streamlit-based web application** that allows users to **manage their book collection** efficiently. Users can **add, remove, search, update read status, and export book data**. It utilizes **SQLite** for data storage and supports filtering by genre, year, and read status.

## Features
✅ **Add Books** – Store books with details like title, author, year, genre, and read status.  
✅ **Remove Books** – Delete books from the library.  
✅ **Search Books** – Find books by title, author, genre, or read status.  
✅ **Update Read Status** – Mark books as **Read** or **Not Read**.  
✅ **View Statistics** – See insights like total books, read books, and reading percentage.  
✅ **Export Data** – Download library data in **CSV format**.

## Technologies Used
- **Python** (Backend logic)
- **Streamlit** (Frontend UI)
- **SQLite** (Database)
- **Pandas** (Data handling)

## Requirnments
Python - 3.12^
streamlit - For building the web interface
sqlite3 - For database management (built into Python)
pandas - For handling tabular data

## Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/Sheikh-Muhammad-Mujtaba/Q3_class_Assignments.git
   cd task-6_Bayt-al-Hikma
   ```
2. **Create a virtual environment** (Optional but recommended)
   ```bash
   python -m venv .venv
   .venv\Scripts\activate    
   ```
3. **Install dependencies**
   ```bash
   uv pip install -r requirements.txt
   ```
4. **Run the application**
   ```bash
   streamlit run library_manager.py
   ```

## Database Schema (`library.db`)
The SQLite database stores books with the following structure:
```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER NOT NULL,
    genre TEXT NOT NULL,
    read_status TEXT NOT NULL CHECK(read_status IN ('Yes', 'No'))
);
```
