""" A utiltiy for pretty console disply """


from pyboxen import boxen


def boxen_result(output, padding=1, margin=1, color="green") -> None:
    """Green result boxen"""
    print(
        boxen(
            output,
            padding=padding,
            margin=margin,
            color=color,
        )
    )


def boxen_info(info, padding=1, margin=1, color="blue") -> None:
    """Blue info boxen"""
    print(
        boxen(
            info,
            padding=padding,
            margin=margin,
            color=color,
        )
    )
