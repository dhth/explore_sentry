from sentry_sdk import add_breadcrumb

def something():
    add_breadcrumb(
        category="db stuff",
        message="Writing to DB",
        level="info",
    )
    return "hello"


def something_else():
    add_breadcrumb(
        category="db stuff",
        message="Writing to DB",
        level="info",
    )
    var1 += sdsdsdsds
    return "hello"


def something_else_2():
    add_breadcrumb(
        category="level1",
        message="Level 1 message",
        level="info",
    )
    var2 += wewewewewe
    return "hello"

