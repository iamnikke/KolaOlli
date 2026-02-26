from queryDb import queryDb

def get_user_location(user_id):

    result = queryDb(f"SELECT location FROM user_info where id = {user_id}")

    return result