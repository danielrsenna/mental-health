
import reflex as rx

from mental_health.states.auth import AuthState
from mental_health.styles.main import style

from . import pages
from .states import navigation
from .states.chat import ChatState

app = rx.App(
    style=style,
    theme=rx.theme(
        # appearance="dark",
        # has_background=True, 
        # panel_background="solid",
        scaling="90%",
        #radius="medium", 
        accent_color="gray",
    )
)

#Website Pages
app.add_page(pages.homepage, navigation.HOME_ROUTE, title="Início")
app.add_page(pages.startherepage, navigation.STARTHERE_ROUTE, title="Comece Aqui")
app.add_page(pages.loginpage, navigation.LOGIN_ROUTE, title="Login")
app.add_page(pages.chatpage, navigation.CHAT_ROUTE, title="Chat", on_load=[AuthState.require_auth, ChatState.on_load])
