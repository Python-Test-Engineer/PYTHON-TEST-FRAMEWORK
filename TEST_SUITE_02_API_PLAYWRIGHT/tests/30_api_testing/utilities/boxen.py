""" A utiltiy for pretty console disply """


from pyboxen import boxen


def bx_result(
    message: str, padding: int = 1, margin: int = 1, color: str = "green"
) -> None:
    """Green result boxen"""
    print(
        boxen(
            message,
            padding=padding,
            margin=margin,
            color=color,
        )
    )


def bx_info(
    message: str, padding: int = 1, margin: int = 1, color: str = "blue"
) -> None:
    """Blue info boxen"""
    print(
        boxen(
            message,
            padding=padding,
            margin=margin,
            color=color,
        )
    )


def bx_warn(
    message: str, padding: int = 1, margin: int = 1, color: str = "red"
) -> None:
    """Red warning boxen"""
    print(
        boxen(
            message,
            padding=padding,
            margin=margin,
            color=color,
        )
    )
