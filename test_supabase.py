from supabase import create_client

SUPABASE_URL = "https://tytzgxgemqvrbqouaynz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InR5dHpneGdlbXF2cmJxb3VheW56Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjA5NDE3NTcsImV4cCI6MjA3NjUxNzc1N30.53SP8OXcexa7rWWOFXF7Pip5CciNtmeVCCpYkwNCyVA"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Test getting data from a table (replace 'books' with your table)
data = supabase.table("books").select("*").execute()
print(data)
