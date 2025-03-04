import reflex as rx

HOME_ROUTE="/"
CHAT_ROUTE="/chatpage"

class NavState(rx.State):
    def to_home(self):
        return rx.redirect(HOME_ROUTE)
    def to_chat(self):
        return rx.redirect(CHAT_ROUTE)



