import reflex as rx


def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon, color="#000000"),
            rx.text(text, size="4", color="#000000",font_weight="bold",font_family= "Garamond"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("gray", 4),
                    "color": rx.color("gray", 11),
                },
                "border-radius": "1em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Início", "layout-dashboard", "/"),
        #sidebar_item("Projects", "square-library", "/#"),
        #sidebar_item("Analytics", "bar-chart-4", "/#"),
        #sidebar_item("Messages", "mail", "/#"),
        spacing="1",
        width="100%",
    )


def sidebar_chat() -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.link(
                    rx.image(
                        src="/sloth_logo_white.jpg",
                        width="3em",
                        height="auto",
                    ),
                    href='/',
                ),
                rx.link(
                    rx.heading(
                        "Kuatan.AI",
                        size="7",
                        weight="bold",
                        font_family= "Garamond",
                        color="#000000",
                    ),
                    href='/', 
                    underline="none",
                ),
                align="center",
                justify="start",
                padding_x="0.5rem",
                width="100%",
            ),
            sidebar_items(),
            rx.spacer(),
            rx.vstack(
                rx.vstack(
                    sidebar_item(
                        "Configurações", "settings", "/#"
                    ),
                    sidebar_item(
                        "Sair", "log-out", "/"
                    ),
                    spacing="1",
                    width="100%",
                ),
                rx.divider(),
                rx.hstack(
                    rx.icon_button(
                        rx.icon("user"),
                        size="3",
                        background="#000000",
                        radius="full",
                    ),
                    rx.vstack(
                        rx.box(
                            rx.text(
                                "Meu Perfil",
                                size="3",
                                weight="bold",
                            ),
                            rx.text(
                                "user@reflex.dev",
                                size="2",
                                weight="medium",
                            ),
                            width="100%",
                        ),
                        spacing="0",
                        align="start",
                        justify="start",
                        width="100%",
                    ),
                    padding_x="0.5rem",
                    align="center",
                    justify="start",
                    width="100%",
                ),
                width="100%",
                spacing="5",
            ),
            spacing="5",
            padding_x="1em",
            padding_y="1.5em",
            bg=rx.color("gray", 1),
            align="start",
            height="100vh",
            width="16em",
        ),
    )
