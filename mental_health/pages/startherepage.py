import reflex as rx

from ..ui import navbar

def startherepage() -> rx.Component:
    # Welcome Page (Index)
    return rx.flex(
        navbar(),
        hero_section(),
        #footer(),
        direction="column",
        justify="center",
        align="center",
        background_color="#ffffff",
    )

def hero_section() -> rx.Component:
    return rx.flex(
        rx.flex(
            rx.flex(
                rx.text(
                    "No que acreditamos;",
                    text_align="left",
                    font_size="30px",
                    font_weight="bold",
                    line_height="1",
                    font_family= "Garamond",
                    color="#000000",  
                    width="100%",
                ),
                rx.flex(
                    rx.text(
                        "Se você está lendo isso, provavelmente busca alguma ajuda. Essa plataforma é para você.",
                        text_align="left",
                        color="#000000", 
                        font_size="20px",
                        font_weight="regular",
                        line_height="1",
                        width="80%",
                        font_family= "Garamond",
                    ),
                    rx.text(
                        "Há pouco mais de 6 anos, fui diagnosticado com depressão, e, desde então, os anos têm sido turbulentos. Talvez você esteja passando por algo similar.",
                        text_align="left",
                        color="#000000", 
                        font_size="20px",
                        font_weight="regular",
                        line_height="1",
                        width="80%",
                        font_family= "Garamond",
                    ),
                    rx.text(
                        "Sei que não é fácil navegar por tudo isso: reconhecer e aceitar o seu momento, buscar ajuda, iniciar um tratamento, persistir no processo, compartilhar suas questões com outras pessoas…",
                        text_align="left",
                        color="#000000", 
                        font_size="20px",
                        font_weight="regular",
                        line_height="1",
                        width="80%",
                        font_family= "Garamond",
                    ),
                    rx.text(
                        "Essa jornada pode ser solitária, confusa e, às vezes, exaustiva. Mas você não precisa percorrê-la sozinho.",
                        text_align="left",
                        color="#000000", 
                        font_size="20px",
                        font_weight="regular",
                        line_height="1",
                        width="80%",
                        font_family= "Garamond",
                    ),
                    rx.text(
                        "Muitas das dificuldades que encontrei ao longo do caminho me fizeram perceber que podemos fazer melhor por quem precisa de apoio. A partir disso, surgiu o desejo de construir algo para mim e para os outros.",
                        text_align="left",
                        color="#000000", 
                        font_size="20px",
                        font_weight="regular",
                        line_height="1",
                        width="80%",
                        font_family= "Garamond",
                    ),
                    rx.text(
                        "Surgiu do desejo genuíno de tornar essa caminhada um pouco mais leve. De ajudar qualquer um, independentemente dos recursos que tenha, a cuidar da sua saúde mental de forma acessível, contínua e eficaz.",
                        text_align="left",
                        color="#000000", 
                        font_size="20px",
                        font_weight="regular",
                        line_height="1",
                        width="80%",
                        font_family= "Garamond",
                    ),
                    direction="column",
                    spacing='2',
                    justify='between',
                    align='stretch',
                ),
                spacing="4",
                direction='column',
                width="50vw",
            ),
            rx.flex(
                rx.text(
                    "Nossos norteadores;",
                    text_align="left",
                    font_size="30px",
                    font_weight="bold",
                    line_height="1",
                    font_family= "Garamond",
                    color="#000000",  
                    width="100%",
                ),
                rx.flex(
                    rx.flex(
                        rx.text(
                            "Pessoas em primeiro lugar",
                            text_align="left",
                            color="#000000", 
                            font_size="20px",
                            font_weight="bold",
                            width="80%",
                            font_family= "Garamond",
                        ),
                        rx.text(
                            "Antes de qualquer tecnologia ou funcionalidade, colocamos as pessoas no centro. A plataforma existe para acolher, apoiar e fazer a diferença na vida real de quem precisa.",
                            text_align="left",
                            color="#000000", 
                            font_size="18px",
                            font_weight="regular",
                            line_height="1",
                            width="80%",
                            font_family= "Garamond",
                            padding_left="1em",
                        ),
                        direction="column",
                    ),
                    rx.flex(
                        rx.text(
                            "Tecnologia como ferramenta de transformação",
                            text_align="left",
                            color="#000000", 
                            font_size="20px",
                            font_weight="bold",
                            width="80%",
                            font_family= "Garamond",
                        ),
                        rx.text(
                            "Acreditamos no poder da tecnologia para facilitar o acesso à saúde mental e aprimorar o cuidado, sem substituir o fator humano, mas sim potencializá-lo.",
                            text_align="left",
                            color="#000000", 
                            font_size="18px",
                            font_weight="regular",
                            line_height="1",
                            width="80%",
                            font_family= "Garamond",
                            padding_left="1em",
                        ),
                        direction="column",
                    ),
                    rx.flex(
                        rx.text(
                            "Foco no que é essencial",
                            text_align="left",
                            color="#000000", 
                            font_size="20px",
                            font_weight="bold",
                            width="80%",
                            font_family= "Garamond",
                        ),
                        rx.text(
                            "Menos é mais. Evitamos distrações e funcionalidades desnecessárias, priorizando o que realmente importa para oferecer uma experiência simples, eficaz e significativa.",
                            text_align="left",
                            color="#000000", 
                            font_size="18px",
                            font_weight="regular",
                            line_height="1",
                            width="80%",
                            font_family= "Garamond",
                            padding_left="1em",
                        ),
                        direction="column",
                    ),
                    rx.flex(
                        rx.text(
                            "Colaboração e transparência",
                            text_align="left",
                            color="#000000", 
                            font_size="20px",
                            font_weight="bold",
                            width="80%",
                            font_family= "Garamond",
                        ),
                        rx.text(
                            "Saúde mental não precisa ser um caminho solitário. Valorizamos a troca entre pessoas, profissionais e a comunidade, promovendo um ambiente de confiança, respeito e acessibilidade.",
                            text_align="left",
                            color="#000000", 
                            font_size="18px",
                            font_weight="regular",
                            line_height="1",
                            width="80%",
                            font_family= "Garamond",
                            padding_left="1em",
                        ),
                        direction="column",
                    ),
                    direction="column",
                    spacing='2',
                    justify='between',
                    align='stretch',
                ),
                spacing="4",
                direction="column",
                width="50vw",
            ),
            direction='row',
            width="100vw",
            padding_left="4em",
            padding_right="4em",
            padding_top="2em",
            padding_bottom="2em",
        ),
        rx.flex(
            rx.link(
                rx.button(
                    "Conhecer",
                    font_size="15px",
                    size="3",
                    weight="bold",
                    variant="solid",
                    radius="full",
                    background_color=rx.color("gray", 12),
                    high_contrast=False,
                ),
                href="/chatpage",
            ),
            align="center",
            spacing="3",
            padding_left="4em",
        ),
        spacing="4",
        direction="column",
        width="100vw",
        justify="start",
        align='stretch',
    )

