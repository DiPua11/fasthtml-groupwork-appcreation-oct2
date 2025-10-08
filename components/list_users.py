
from fasthtml.common import *

def create_user_row(user):
    return Tr(
        Td(user['first_name']), 
        Td(user['last_name']),
        Td(Button ("Delete"))
    )

def list_users_table(users):
    rows = [create_user_row (user) for user in users]
    return Titled(
        "List Users", 
        Table(
            Thead(Tr(Th("First Name"), Th("Last Name"), Th("Action"))),
            Tbody(*rows)
        )
    )
