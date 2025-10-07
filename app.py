from fasthtml.common import *
from pages.page1 import get_page1
from pages.page2 import get_page2

app, rt = fast_app()

@rt("/page1")
def page1():
    return get_page1()

@rt("/page2")
def page2():
    return get_page2

serve()

# from fasthtml.common import *
# from pages.page1 import add_user_page
# from pages.page2 import list_users_page

# app, rt = fast_app()

# list_of_users = [
#     {"first_name": "Diana", "last_name": "DeRego"}
#     {"first_name": "Greg", "last_name": "Clay"}
#     {"first_name": "John", "last_name": "Doe"}
# ]

# @rt("/")
# def get():
#     return add_user_page()
#     # return Titled(
#     #     "Main Page",
#     #         Div("Add User"),
#     #         Hr(),
#     #         Div(f"The number of users in my database are {len([])}")
#     # )

# @rt("/page2")
# def get():
#     return list_users_page(list_of_users)

# # @rt("/list_users_page")
# # def get():
# #      return Titled(
# #          "List Users",
# #          Div("Listing users...")
# #      )

# # @rt("/")
# # def get():
# #     return Div("Hello World")

# #"""This is working"""
# # @rt("/list_users")
# # def list_users():
# #     return Titled(
# #         "List Users",
# #         Div("Listing users...")
# #     )

# # @rt("/diana")
# # def get():
# #     return Titled(
# #         "Diana's Page",
# #         P("Listing Users")
# #     )

# serve()

