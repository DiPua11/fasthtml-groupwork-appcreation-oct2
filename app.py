from fasthtml.common import *

app, rt = fast_app()

# @rt("/")
# def get():
#     return Div("Hello World")

#"""This is working"""
# @rt("/list_users")
# def list_users():
#     return Titled(
#         "List Users",
#         Div("Listing users...")
#     )

@rt("/")
def get():
    return Titled(
        "Main Page",
            Div("Add User"),
            Hr(),
            Div(f"The number of users in my database are {len([])}")
    )

# @rt("/")
# def get():
#     return Titled(
#         "Main Page",
#         P("Listing Users")
#     )

serve()

