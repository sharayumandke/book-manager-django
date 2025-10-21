from supabase import create_client

SUPABASE_URL = "https://tytzgxgemqvrbqouaynz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR5dHpneGdlbXF2cmJxb3VheW56Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA5NDE3NTcsImV4cCI6MjA3NjUxNzc1N30.53SP8OXcexa7rWWOFXF7Pip5CciNtmeVCCpYkwNCyVA"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Example CRUD functions

def get_books():
    return supabase.table("books").select("*").execute()

def add_book(title, author, published_date):
    return supabase.table("books").insert({
        "title": title,
        "author": author,
        "published_date": published_date
    }).execute()

def update_book(book_id, title=None, author=None):
    updates = {}
    if title:
        updates["title"] = title
    if author:
        updates["author"] = author
    return supabase.table("books").update(updates).eq("id", book_id).execute()

def delete_book(book_id):
    return supabase.table("books").delete().eq("id", book_id).execute()
