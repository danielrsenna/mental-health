import reflex as rx


style = {
    'font_family': 'Segoe UI (Custom)',
    'color': rx.color('gray', 12),
    rx.text: {
        'size': '4',
    },
    rx.heading: {
        'font_family': 'Garamond',
        'size': '7',
        'weight': 'bold',
    },
    rx.icon: {
        'color': rx.color('gray', 12),
    },
    rx.link: {
        'font_family': 'Garamond',
        'color': rx.color('gray', 12),
        'underline': 'none',
        'weight': 'bold',
    },
    rx.button: {
        'weight': 'bold',
        'color': rx.color('gray', 1),
        'background_color': rx.color('gray', 12),
        '_hover': {
            'background_color': rx.color('gray', 11),
        },
        'cursor': 'pointer',
    }
}
