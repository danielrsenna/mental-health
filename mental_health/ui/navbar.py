import reflex as rx
#from .. import navigation

def navbar() -> rx.Component:
    return rx.flex( #navbar como um todo
            rx.flex( #(logo+nome) + Sobre
                rx.flex( #esquerda da navbar logo+nome
                    rx.link( #logo
                        rx.image(
                            src="/sloth_logo_green.jpg",
                            width="2.25em",
                            height="auto",
                            border_radius="25%",
                        ),
                        #href=navigation_web.routes.HOME_ROUTE
                        href="/",
                    ),
                    rx.link( #nome
                        rx.heading(
                            "Kuatan", 
                            size="7", 
                            weight="bold",
                            color=rx.color("black", 12), #trocar para preto
                        ),
                        #href=navigation_web.routes.HOME_ROUTE,
                        href="/",
                        underline="none",
                    ),
                    spacing="2",
                ),
                rx.flex( #select Sobre
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.hstack(
                                    rx.text("Sobre",color="#000000",weight="medium"), #trocar para preto
                                    rx.icon("chevron-down", size=15,color="#000000"), #trocar para preto
                                align="center",
                                ),
                                variant="ghost",
                                radius="full",
                                color_scheme=("gray"),#mudar essa cor
                                size="3",
                            ),
                        ),
                        rx.menu.content(
                             rx.menu.item(rx.link(rx.text("Quem somos", color="#000000"), underline="none", href="/chatpage"),),
                            rx.menu.item(rx.link(rx.text("Perguntas Frequentes", color="#000000"), underline="none", href="/chatpage"),),
                            rx.menu.item(rx.link(rx.text("Preços", color="#000000"), underline="none", href="/chatpage"),),
                            color_scheme="gray", #mudar essa cor
                        ),
                    ),
                ),
                spacing="7",
                align="center",
            ),
            rx.flex( #botões entrar+cadastrar
                rx.link( #botão entrar
                    rx.button(
                        "Entrar",
                        size="3",
                        weight="medium",
                        variant="solid",
                        radius="full",
                        color_scheme=("gray"), #mudar essa cor
                        high_contrast=False,
                    ),
                    #href=navigation_web.routes.LOGIN_ROUTE
                    href="/chatpage",
                ),
                rx.link( #botão cadastrar
                    rx.button(
                        rx.text("Criar Conta",color="#ffffff",weight="medium"), #mudar essa cor
                        size="3",
                        variant="ghost",
                        radius="full",
                        high_contrast=False,
                        color_scheme=("gray"), #mudar essa cor
                    ),
                    #href=navigation_web.routes.REGISTER_ROUTE
                    href="/chatpage",
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

    