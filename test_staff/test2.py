import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])

var1 = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]


# result_list = []
# for i in var1:
#     string_list = []
#     for j in i.values():
#         string_list.append(j)
#     cat = Cat(*string_list)
#     result_list.append(cat)


def convert_list(cats):
    if isinstance(cats[0], dict):
        result_list = []
        for i in cats:
            string_list = []
            for j in i.values():
                string_list.append(j)
            cat = Cat(*string_list)
            result_list.append(cat)
        return result_list
    else:
        result_list = list()
        for i in cats:
            string_dict = dict()
            for j in range(len(i)):
                string_dict.update({i._fields[j]: i[j]})
            result_list.append(i._asdict())
        return result_list

# print(var1)

var2 = convert_list(var1)


print(convert_list(var2))
