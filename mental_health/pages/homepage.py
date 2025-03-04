import reflex as rx

from ..ui import navbar, footer, hero_section

def homepage() -> rx.Component:
    # Welcome Page (Index)
    return rx.flex(
        navbar(),
        hero_section(),
        footer(),
        direction="column",
        align="center",
        background_color="#ffffff",
    )
