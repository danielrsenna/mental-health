
import reflex as rx

from . import pages
from . import navigation

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
app.add_page(pages.homepage, navigation.routes.HOME_ROUTE, title="Homepage")
app.add_page(pages.chatpage, navigation.routes.CHAT_ROUTE, title="Chat")


