import reflex as rx

HOME_ROUTE='/'
AUTH_ROUTE='/auth'
CHAT_ROUTE='/chatpage'
LOGIN_ROUTE='/login'
STARTHERE_ROUTE='/comeceaqui'

class NavState(rx.State):
    def to_home(self):
        return rx.redirect(HOME_ROUTE)
    def to_chat(self):
        return rx.redirect(CHAT_ROUTE)
    def to_starthere(self):
        return rx.redirect(STARTHERE_ROUTE)
    def to_login(self):
        return rx.redirect(LOGIN_ROUTE)



