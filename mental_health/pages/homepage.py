import reflex as rx

from ..ui import navbar, footer
from ..states import navigation

def homepage() -> rx.Component:
    # Welcome Page (Index)
    return rx.flex(
        navbar(),
        hero_section(),
        #footer(),
        direction="column",
        justify="center",
        align="center",
        background_color="#ffffff",
        height="100vh",
    )

def hero_section() -> rx.Component:
    """Render the hero section of the landing page."""
    return rx.flex(
        rx.text(
            "Saúde mental acessível para todos.",
            text_align="left",
            #background_image="linear-gradient(95deg, #D6D6ED 42.14%, #727280 63.21%)",
            font_size="40px",
            #background_clip="text",
            font_weight="bold",
            line_height="1",
            font_family= "Garamond",
            #background_color="#000000",
            color="#000000",  
            width="50%",
        ),
        # rx.text(
        #     "Kuatan fará isso realidade. É como ajudaremos você em seu caminho.",
        #     text_align="left",
        #     color="#000000", 
        #     #background_color="#000000",
        #     font_size="30px",
        #     font_family= "Garamond",
        #     font_weight="bold",
        #     line_height="1",
        #     #max_width=["300px", "350px", "650px", "650px", "650px", "650px"],
        # ),
        rx.text(
            "Kuatan Saúde: Uma plataforma para pacientes, para psicólogos, para você.",
            text_align="left",
            color="#000000", 
            #background_color="#000000",
            font_size="30px",
            font_family= "Garamond",
            font_weight="bold",
            line_height="1",
            #max_width=["300px", "350px", "650px", "650px", "650px", "650px"],
        ),
        rx.link(
            rx.button(
                "Conhecer",
                font_size="15px",
                #font_family= "Garamond",
                size="3",
                weight="bold",
                variant="solid",
                radius="full",
                background_color=rx.color("gray", 12),
                high_contrast=False,
            ),
            href=navigation.LOGIN_ROUTE,
        ),
        spacing="2",
        direction="column",
        #background_color="red",
        height="100vh",
        width="100vw",
        justify="center",
        align="start",
        padding="5em",
    )
