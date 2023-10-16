def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        first_part = ", ".join(items[:-1])
        last_part = f", and {items[-1]}"
        return f"{first_part}{last_part}"

