from fasthtml.common import *
from contents.user_form import user_form
from contents.db_contents import db_contents
from contents.records import records_page

app, rt = fast_app()

# Fake in-memory DB
users = []

# -------------------
# Home Page: User Entry
# -------------------
@rt("/")
def home():
    return Titled(
        "First Page",
        #user_form
            user_form(),
            Hr(),
            # Activity & Status
            db_contents(users)
        )
    

# -------------------
# Submit User (Form POST)
# -------------------
@rt("/submit", methods=["POST"])
def submit(first_name: str, last_name: str):
    users.append({"first": first_name, "last": last_name})
    return Redirect("/")

# -------------------
# Records Page
# -------------------
@rt("/records")
def records():
    return  records_page(users)

serve()
