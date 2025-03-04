import reflex as rx

def hero_section() -> rx.Component:
    """Render the hero section of the landing page."""
    return rx.flex(
        rx.text(
            "O acesso à saúde mental é um direito de todos.",
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
        rx.text(
            "Kuatan é a nossa forma de contribuir para isso.",
            text_align="left",
            color="#000000", 
            #background_color="#000000",
            font_size="30px",
            font_family= "Garamond",
            font_weight="bold",
            line_height="1",
            #max_width=["300px", "350px", "650px", "650px", "650px", "650px"],
        ),
        rx.text(
            "Uma plataforma para profissionais, para pacientes, para todas as pessoas.",
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
                "Começar",
                color_scheme=("gray"), #mudar cor
                size="4",
            ),
            href="/chatpage",
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

