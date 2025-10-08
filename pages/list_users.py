from fasthtml.common import *
from components.list_users import list_users_table

def list_users_page(users):
    return list_users_table(users)

# GROUPWORK CODE WITH NICK AND MARITZA - 2nd ATTEMPT
# def get_page2(): 
#     # Sample data
#     users = [
#     {'id': 1, 'username': 'diana_derego', 'email': 'diana@example.com'},
#     {'id': 2, 'username': 'gclayton', 'email': 'greg@example.com'},
#     {'id': 3, 'username': 'jane_doe', 'email': 'jane@example.com'},
# ]

# @rt("/")
# def get():
#     return Titled("User Table",
#         H2("User List"),
#         Table(
#             Thead(
#                 Tr(
#                     Th("ID", style="padding: 10px; border: 1px solid #ddd;"),
#                     Th("Username", style="padding: 10px; border: 1px solid #ddd;"),
#                     Th("Email", style="padding: 10px; border: 1px solid #ddd;")
#                 )
#             ),))

# from fasthtml.common import *
    
# def list_users_page(list_of_users):
#     return Titled("User Table", P("Listing users..."))

#  serve()