""" A utiltiy for pretty console disply """


from pyboxen import boxen


def bx_result(message, padding=1, margin=1, color="green") -> None:
    """Green result boxen"""
    print(
        boxen(
            message,
            padding=padding,
            margin=margin,
            color=color,
        )
    )


def bx_info(message, padding=1, margin=1, color="blue") -> None:
    """Blue info boxen"""
    print(
        boxen(
            message,
            padding=padding,
            margin=margin,
            color=color,
        )
    )


def bx_warn(message, padding=1, margin=1, color="red") -> None:
    """Blue warning boxen"""
    print(
        boxen(
            message,
            padding=padding,
            margin=margin,
            color=color,
        )
    )
