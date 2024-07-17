from utility.UtilityText import UtilityText

class ListUtility:

    def find_in_list_by_name(list_to_search, name):
        return next(iter(structure for structure in list_to_search if structure.name == name), None)

    def find_in_list_by_part_name(list_to_search, name):
        return next(iter(structure for structure in list_to_search if name in structure.name), None)

    def find_in_list_by_part_name_ignore_case(list_to_search, name):
        return next(iter(structure for structure in list_to_search if name.upper() in structure.name.upper()), None)

    def find_in_list_by_string(list_to_search, string_to_find):
        return next(iter(item for item in list_to_search if string_to_find in item), None)

    def find_index(list_to_search, item):
        try:
            index = list_to_search.index(item)
        except ValueError:
            index = -1
        return index

    def find_similar_index(list_to_search, item):
        counter = 0
        found = False
        while counter < len(list_to_search) and not found:
            if UtilityText.similar_line(item, list_to_search[counter], 0.6):
                found = True
            counter += 1
        return found

    def add_to_unique_list(list_to_add, item_to_add):
        if ListUtility.find_in_list_by_name(list_to_add, item_to_add.name) == None:
            list_to_add.append(item_to_add)

    def format_list(list_to_format, display, spacer="; "):
        return display + ListUtility.format_list_name(list_to_format, spacer)

    def format_list_name(list_to_format, spacer="; "):
        prefix = ""
        suffix = "."
        display = ""
        for item in list_to_format:
            if prefix == "":
                display += item.get_class_name() + ":- "
            display += prefix + item.get_name()
            if prefix == "":
                prefix = spacer
        return display + suffix

    def at_least_one_match_between_lists(first_list, second_list):
        found = False
        counter = 0
        while not found and counter < len(second_list):
            if second_list[counter] in first_list:
                found = True
            counter += 1
        return found

    def compare_lists(to_list, from_list):
        missing_list = []
        for item in from_list:
            if item not in to_list:
                missing_list.append(item)
        return set(missing_list)
    
    def compare_lists_by_name(to_list, from_list):
        missing_list = []
        found_item = None
        for item in from_list:
            found_item = ListUtility.find_in_list_by_name(to_list, item.get_name())
            if found_item is None:
                missing_list.append(item)
        return set(missing_list)

    def same_lists(from_list, to_list):
        same_list = []
        for item in from_list:
            if item in to_list:
                same_list.append(item)
        return set(same_list)
    
    def same_lists_by_name(to_list, from_list):
        same_list = []
        found_item = None
        for item in from_list:
            found_item = ListUtility.find_in_list_by_name(to_list, item.get_name())
            if found_item is not None:
                same_list.append(item)
        return set(same_list)