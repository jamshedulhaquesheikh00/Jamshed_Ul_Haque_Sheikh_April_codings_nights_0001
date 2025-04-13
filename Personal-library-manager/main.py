import streamlit as st  # Import Streamlit for UI
import pandas as pd  # Data handling
import random  # For unique IDs

# Initialize session state for storing books
if "library" not in st.session_state:
    st.session_state.library = []

# Function to add book
def add_book(title, author, genre, status):
    book = {"ID": random.randint(1000, 9999), "Title": title, "Author": author, "Genre": genre, "Status": status}
    st.session_state.library.append(book)

# Function to delete book
def delete_book(book_id):
    st.session_state.library = [book for book in st.session_state.library if book["ID"] != book_id]

# Function to mark book as read
def mark_as_read(book_id):
    for book in st.session_state.library:
        if book["ID"] == book_id:
            book["Status"] = "Read"

# Sidebar Navigation
st.sidebar.title("📚 Library Manager")
option = st.sidebar.selectbox("Select an option", ["🏠 Home", "➕ Add Book", "🔍 Search Book", "✔ Mark as Read", "❌ Delete Book"])

# Right Side Content Based on Selection
st.title(option)  # Page Title Changes Based on Selected Option

if option == "🏠 Home":
    st.subheader("Welcome to Personal Library Manager!")
    st.write("Easily manage your books, track reading status, and organize your collection.")
    st.write("Use the sidebar to navigate different sections. 📖")
    
    if st.session_state.library:
        st.subheader("📌 Your Library")
        df = pd.DataFrame(st.session_state.library)
        st.write(df)
    else:
        st.write("No books added yet.")

elif option == "➕ Add Book":
    st.subheader("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author Name")
    genre = st.text_input("Genre")
    status = st.selectbox("Status", ["Unread", "Read"])

    if st.button("Add Book"):
        add_book(title, author, genre, status)
        st.success("✅ Book Added!")

elif option == "🔍 Search Book":
    st.subheader("Search for a Book")
    search_query = st.text_input("Enter book title or author")
    
    if search_query:
        search_results = [book for book in st.session_state.library if search_query.lower() in book["Title"].lower() or search_query.lower() in book["Author"].lower()]
        if search_results:
            st.write(pd.DataFrame(search_results))
        else:
            st.write("No matching books found.")

elif option == "✔ Mark as Read":
    st.subheader("Mark a Book as Read")
    book_id_read = st.number_input("Enter Book ID", min_value=1000, max_value=9999, step=1)
    
    if st.button("Mark as Read"):
        mark_as_read(book_id_read)
        st.success("📗 Book marked as Read!")

elif option == "❌ Delete Book":
    st.subheader("Delete a Book")
    book_id_delete = st.number_input("Enter Book ID to Delete", min_value=1000, max_value=9999, step=1)

    if st.button("Delete Book"):
        delete_book(book_id_delete)
        st.warning("🗑 Book Deleted!")

st.sidebar.write("📌 Built with ❤ by [Summiya](https://github.com/Summiyaashraf)")
