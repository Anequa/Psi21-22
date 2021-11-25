from graphql_jwt.decorators import user_passes_test


def is_admin(function=None):

    actual_decorator = user_passes_test(
        lambda user: user.groups.filter(name="administrators").exists()
    )

    if function:
        return actual_decorator(function)
    return actual_decorator
