def flights(*args):
    result = {}

    for idx in range(0, len(args) - 1, 2):
        destination = args[idx]
        passengers = args[idx + 1]

        if destination == "Finish":
            break

        elif destination not in result:
            result[destination] = passengers

        else:
            result[destination] += passengers

    return result
