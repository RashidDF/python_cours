user_data = ['Bogdan', 152]


def user_info(name, comments_qty):
    if not comments_qty:
        return f"{name} has no comments"
    return f"{name} has {comments_qty} comments"


print(user_info(*user_data))

print(user_info(user_data[0], user_data[1]))
