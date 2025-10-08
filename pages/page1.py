from fasthtml.common import *

@rt("/")
def get():
    return Titled(
        "Page 1",
        Div("Add User"),
        Hr(),
        Div ("The number of users in my database are X") )

serve()


# GROUPWORK CODE WITH NICK AND MARITZA - 2nd ATTEMPT
# def get_page1(): 
#     return Titled(
#         "Page 1",
#           H2("This is Page 1"),
#             P("Welcome to the first page!"),
#             P("You can add more content here."),
#             Hr(),
#             A("Go to Page 2", href="/page2") )

# FIRST ATTEMPT FOLLOWING CLASS VIDEO
# from fasthtml.common import *
# def add_user_page(list_of_users):
#     rows = []
#     for user in list_of_users:
#         rows.append(Tr(
#             Td(user["first_name"]),
#             Td(user["last_name"])
#         ))
    
#     return Titled("List Users",
#         Table(
#             Thead(
#                 Tr(Th("First Name"), Th("Last Name"))
#             ),
#             Tbody(*rows)
#         )

#     # return Titled("Main Page", Div("Add User Section"), Hr(), Div(f"The number of users in my database are {len([])}")
#     # )

#     serve()