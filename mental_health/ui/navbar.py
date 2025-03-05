import reflex as rx
from ..states import navigation

def navbar() -> rx.Component:
    return rx.flex( #navbar como um todo
            rx.flex( #(logo+nome) + Sobre
                rx.flex( #esquerda da navbar logo+nome
                    rx.link( #logo
                        rx.image(
                            src="/sloth_logo_white.jpg",
                            width="4em",
                            height="auto",
                            #border_radius="25%",
                        ),
                        href=navigation.HOME_ROUTE,
                    ),
                    rx.link( #nome
                        rx.text(
                            "Kuatan Saúde",
                            font_size="30px",
                            font_family= "Garamond",
                            weight="bold",
                            color="#000000",
                        ),
                        href=navigation.HOME_ROUTE,
                        underline="none",
                    ),
                    spacing="1",
                    align="center",
                    justify="center",
                ),
                align="center",
                justify="between",
            ),
            rx.cond(
                rx.State.router.page.path != '/comeceaqui',
                rx.flex(
                    rx.link( #nome
                        rx.text(
                            "Comece aqui",
                            font_size="18px",
                            #font_family= "Garamond",
                            weight="bold",
                            color="#000000",
                        ),
                        href=navigation.STARTHERE_ROUTE,
                        underline="hover",
                    ),
                ),
            ),
            rx.flex( #botão à direita
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
                    #href=navigation_web.routes.LOGIN_ROUTE
                    href=navigation.CHAT_ROUTE,
                ),
                align="center",
                spacing="3",
                #padding_left="0.5em",    
            ),
            align="center",
            padding_top="0.5em",
            padding_bottom="0.5em",
            padding_left="2em",
            padding_right="2em",
            justify="between",
            #background_color="blue",
            width="99.5%",
        )

    