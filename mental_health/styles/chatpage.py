import reflex as rx

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.15) 0px 2px 8px"
chat_margin = "5%"
message_style = dict(
    padding="1em",
    border_radius="8px",
    margin_y="0.5em",
    #box_shadow=shadow,
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left=chat_margin,
    background_color=rx.color("gray", 6),
)
answer_style = message_style | dict(
    margin_right=chat_margin,
    background_color=rx.color("gray", 4),
)

# Styles for the action bar.
input_style = dict(
    border_width="1px",
    padding="0.5em",
    box_shadow=shadow,
    width="40vw",
    height="5vh",
)
button_style = dict(
    box_shadow=shadow,
    height="5vh",
)
