import sqlite3
import streamlit as st
import pandas as pd
import requests

# Custom CSS for styling and config
st.set_page_config(page_title="Personal Library Manager", page_icon="📚", layout="wide")

def load_css():
    with open("styles.css", "r") as file:
        css = file.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

# Call the function at the beginning
load_css()

# Database Initialization
def init_db():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL,
        genre TEXT NOT NULL,
        read_status TEXT NOT NULL CHECK(read_status IN ('Yes', 'No'))
    )
    """)
    conn.commit()
    conn.close()

# Function to add a book
def add_book(title, author, year, genre, read_status):
    read_status = "Yes" if read_status else "No"
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year, genre, read_status) VALUES (?, ?, ?, ?, ?)", 
                   (title, author, year, genre, read_status))
    conn.commit()
    conn.close()

# Function to remove a book
def remove_book(title):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE title = ?", (title,))
    rows_deleted = cursor.rowcount
    conn.commit()
    conn.close()
    return rows_deleted > 0

# Function to fetch all books
def get_books():
    conn = sqlite3.connect("library.db")
    df = pd.read_sql_query("SELECT * FROM books", conn)
    conn.close()
    return df

# Function to search books
def search_books(search_type, query, genre_filter=None, year_filter=None, read_status_filter=None):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    query = f"%{query}%"
    sql = "SELECT * FROM books WHERE 1=1"
    params = []

    if search_type == "Title":
        sql += " AND title LIKE ?"
        params.append(query)
    elif search_type == "Author":
        sql += " AND author LIKE ?"
        params.append(query)

    if genre_filter:
        sql += " AND genre = ?"
        params.append(genre_filter)

    if year_filter:
        sql += " AND year = ?"
        params.append(year_filter)

    if read_status_filter is not None:
        sql += " AND read_status = ?"
        params.append(read_status_filter)

    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()
    return results

# Function to update book read status
def update_read_status(title, read_status):
    read_status = "Yes" if read_status else "No"
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET read_status = ? WHERE title = ?", (read_status, title))
    rows_updated = cursor.rowcount
    conn.commit()
    conn.close()
    return rows_updated > 0


# Function to display statistics
def get_statistics():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM books")
    total_books = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM books WHERE read_status = 'Yes'")
    read_books = cursor.fetchone()[0]

    conn.close()

    read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
    return total_books, read_books, round(read_percentage, 2)

# Initialize database
init_db()

# Streamlit UI
st.title("📚 Personal Library Manager")

# Sidebar Navigation
menu = ["🏠 Home", "➕ Add Book", "🗑️ Remove Book", "🔍  Search Books", "📌 Update Read Status", "📊 Statistics", "📥 Export Data"]
choice = st.sidebar.radio("Navigation", menu)

# Home - Display all books
if choice == "🏠 Home":
    st.subheader("📖 All Books in Library")
    books_df = get_books()
    if books_df.empty:
        st.warning("No books found. Add some books first.")
    else:
        st.dataframe(books_df)

# Add a Book
elif choice == "➕ Add Book":
    st.subheader("➕ Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Book Title", placeholder="Enter title")
        author = st.text_input("Author", placeholder="Enter author")
        year = st.number_input("Publication Year", min_value=1500, max_value=2025, step=1)
        genre = st.text_input("Genre", placeholder="Enter genre")
        read_status = st.radio("Read Status", ["No", "Yes"])
        submitted = st.form_submit_button("Add Book")
    
    if submitted:
        add_book(title, author, year, genre, read_status)
        st.success(f"Book '{title}' added successfully!")

# Remove a Book
elif choice == "🗑️ Remove Book":
    st.subheader("🗑️ Remove a Book")
    books_df = get_books()
    if books_df.empty:
        st.warning("No books available to remove.")
    else:
        book_titles = books_df["title"].tolist()
        title_to_remove = st.selectbox("Select a book to remove", book_titles)
        if st.button("Remove Book"):
            if remove_book(title_to_remove):
                st.success(f"Book '{title_to_remove}' removed successfully!")
            else:
                st.error("Error removing book. Try again.")

# Search Books
elif choice == "🔍  Search Books":
    st.subheader("🔍 Search for a Book")
    search_type = st.radio("Search By", ("Title", "Author"))
    query = st.text_input("Enter Search Term", placeholder="Enter keyword")
    genre_filter = st.text_input("Filter by Genre", placeholder="Enter genre")
    year_filter = st.number_input("Filter by Year", min_value=1500, max_value=2025, step=1, value=None)
    read_status_filter = st.radio("Filter by Read Status", ("All", "Read", "Not Read"))
    read_status_filter = None if read_status_filter == "All" else (read_status_filter == "Read")

    if st.button("Search"):
        results = search_books(search_type, query, genre_filter, year_filter, read_status_filter)
        if results:
            st.success(f"Found {len(results)} matching book(s):")
            df_results = pd.DataFrame(results, columns=["ID", "Title", "Author", "Year", "Genre", "Read Status"])
            st.dataframe(df_results)
        else:
            st.warning("No books found matching your search.")

# Update Read Status
elif choice == "📌 Update Read Status":
    st.subheader("📌 Update Read Status")
    books_df = get_books()
    if books_df.empty:
        st.warning("No books available to update.")
    else:
        book_titles = books_df["title"].tolist()
        selected_book = st.selectbox("Select a book", book_titles)
        new_status = st.radio("New Read Status", ("Not Read", "Read")) == "Read"
        if st.button("Update Status"):
            if update_read_status(selected_book, new_status):
                st.success(f"Read status updated for '{selected_book}'!")
            else:
                st.error("Error updating book. Try again.")

# Display Statistics
elif choice == "📊 Statistics":
    st.subheader("📊 Library Statistics")
    total_books, read_books, read_percentage = get_statistics()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Books", total_books)
    with col2:
        st.metric("Books Read", read_books)
    with col3:
        st.metric("Reading Completion", f"{read_percentage}%")

    if total_books > 0:
        st.progress(read_percentage / 100)

# Export Data
elif choice == "📥 Export Data":
    st.subheader("📥 Export Library Data")
    books_df = get_books()
    if books_df.empty:
        st.warning("No books available to export.")
    else:
        st.download_button(
            label="Download CSV",
            data=books_df.to_csv(index=False),
            file_name="library_data.csv",
            mime="text/csv"
        )