import streamlit as st

st.title("Приложение")

# Създаваме масив (списък), ако още не съществува
if "books" not in st.session_state:
    st.session_state.books = []

# ============================
# ➕ Добавяне на книга
# ============================

st.header("➕ Добави книга")
title = st.text_input("Заглавие")
author = st.text_input("Автор")
price = st.number_input("Цена", min_value=0.0)

if st.button("Добави книгата"):
    book = {
        "title": title,
        "author": author,
        "price": price
    }

    st.session_state.books.append(book)
    st.success("Книгата е добавена!")

# ============================
# 🔎 Търсене по автор
# ============================

st.header("🔎 Търсене по автор")
search_author = st.text_input("Въведи име на автор")

if st.button("Търси по автор"):
    found = False

    for book in st.session_state.books:
        if book["author"] == search_author:
            st.write(book)
            found = True

    if found == False:
        st.write("Няма намерени книги от този автор.")

# ============================
# 📚 Покажи всички книги
# ============================

if st.button("Покажи всички книги"):
    if len(st.session_state.books) == 0:
        st.write("Няма добавени книги.")
    else:
        for book in st.session_state.books:
            st.write("Заглавие:", book["title"])
            st.write("Автор:", book["author"])
            st.write("Цена:", book["price"])
            st.write("--------------------")

# ============================
# 🔎 Търсене по заглавие
# ============================

st.header("🔎 Търсене по заглавие")
search_title = st.text_input("Въведи заглавие на книга")

if st.button("Търси по заглавие"):
    found = False

    for book in st.session_state.books:
        if book["title"].lower() == search_title.lower():
            st.write(book)
            found = True

    if not found:
        st.write("Няма намерена книга с това заглавие.")

# ============================
# 💰 Търсене по цена
# ============================

st.header("💰 Търсене по цена")
search_price = st.number_input("Въведи цена за търсене", min_value=0.0, key="price_search")

if st.button("Търси по цена"):
    found = False

    for book in st.session_state.books:
        if book["price"] == search_price:
            st.write(book)
            found = True

    if not found:
        st.write("Няма книги с тази цена.")
