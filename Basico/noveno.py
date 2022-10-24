

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not Found"
        case 200:
            return "Ok"
        case 201|202|210:
            return "No tengo ni idea"
        case 304:
            return "No recharge"
        case _:
            return "Algo esta mal!!"