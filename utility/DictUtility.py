class DictUtility:

    def dict_remove_items(original, duplicates):
        return {key: value for key, value in original.items() if key not in duplicates}
    
    def dict_format(data_dict):
        content = str(data_dict)
        replace_pairs = {
            "{": "",
            "}": "",
            "[": "",
            "]": "\n",
            ": ": "\n",
        }   
        return content
