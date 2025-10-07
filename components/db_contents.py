from fasthtml.common import *

def db_contents(users: list):
    return Div(
    H3("Activity & Status"),
    Div(
        f"Currently DB contains {len(users)} entries"
        ),
    Br(),
    A("View All Entries", href="/records")
    )

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