
from fasthtml.common import *

def records_page(users: list):
    return Titled(
        "Second Page - User Records",
        Div(
            H2("User Records"),

            # Table of entries
            Table(
                Thead(
                    Tr(Th("FIRST NAME"), Th("LAST NAME"))
                ),
                Tbody(
                    *[Tr(Td(u["first"]), Td(u["last"])) for u in users]
                )
            ),
            Br(),
            A("< Back to Input", href="/"),
        )
    )
