
import reflex as rx

from . import pages
from .states import navigation
from .states.chat import ChatState

app = rx.App(
    theme=rx.theme(
        #appearance="light", 
        # has_background=True, 
        # panel_background="solid",
        scaling="90%",
        #radius="medium", 
        #accent_color="bronze",
    )
)

#Website Pages
app.add_page(pages.homepage, navigation.HOME_ROUTE, title="Homepage")
app.add_page(pages.chatpage, navigation.CHAT_ROUTE, title="Chat", on_load=ChatState.on_load)
