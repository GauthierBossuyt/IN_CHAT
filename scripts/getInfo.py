import ast


def getCreds():
    file = open("settings/credentials.txt", "r")
    content = file.read()
    credentials = ast.literal_eval(content)
    file.close()
    return credentials

