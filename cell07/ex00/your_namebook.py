def array_of_names(names):
    return [f"{first.capitalize()} {last.capitalize()}" for first, last in names.items()]

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
