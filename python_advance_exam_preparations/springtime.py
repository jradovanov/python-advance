
def movie_organizer(**kwargs):
    result = ""
    items_types = {}

    for key, value in kwargs.items():
        if value not in items_types:
            items_types[value] = []
        items_types[value].append(key)

    sorted_items = sorted(items_types.items(), key=lambda x: (-len(x[1]), x[0]))

    for x in sorted_items:
        type_item = x[0]
        items_list = x[1]
        sorted_list_items = sorted(items_list)
        result += f"{type_item}:\n"
        for y in sorted_list_items:
            result += f"-{y}\n"

    return result.strip()


print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))





























# def start_spring(**kwargs):
#     collections = {}
#
#     for obj, obj_type in kwargs.items():
#         if obj_type not in collections:
#             collections[obj_type] = []
#         collections[obj_type].append(obj)
#
#     sorted_collections = list(collections.items())
#     sorted_collections.sort(key=sort_key)
#
#     for collection in sorted_collections:
#         collection[1].sort()
#
#     result = ""
#     for obj_type, objects in sorted_collections:
#         result += f"{obj_type}:\n"
#         for obj in objects:
#             result += f"-{obj}\n"
#
#     return result.strip()
#
# def sort_key(item):
#     return (-len(item[1]), item[0])