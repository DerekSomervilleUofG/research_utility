import re

class UtilityText:

    def get_non_blank_lines(self, content):
        content = content.replace('\n\n\n', '\n').replace('\n\n', '\n')
        lines = [line for line in content.split('\n') if line.strip() != '']
        return lines

    def case_to_word(self, cased_word):
        words = []
        if "_" in cased_word:
            words = self.break_snake_case(cased_word)
        else:
            words = self.break_camel_case(cased_word)
        return words

    def break_snake_case(self, snake_case):
        return snake_case.split("_")

    def break_camel_case(self, camel_case):
        words = []
        new_word = ""
        for letter in camel_case:
            if len(new_word) == 0 or letter.isupper():
                if len(new_word) > 0:
                    words.append(new_word.lower())
                new_word = letter
            else:
                new_word += letter
        words.append(new_word.lower())
        return words

    def change_camel_case_to_snake(self, word):
        return "_".join(self.break_camel_case(word))

    def make_hyper_link(self, url, name):
        return '<a href="' + url + '">' + name + '</a>'

    def generate_words(raw_line):
        initial_words = re.split(' |, |{|}|\t|-|_|!|:|;|\.|\(|\)', raw_line)
        no_zero_words = UtilityText.remove_zero_length_words(initial_words)
        return no_zero_words
    
    def find_string_in_lines_words(find_string, lines):
        found = False
        counter = 0
        while counter < len(lines) and not found:
            if find_string in UtilityText.generate_words(lines[counter]):
                found = True
            counter += 1
        return found

    def find_string_in_lines(find_string, lines):
        found = False
        counter = 0
        while counter < len(lines) and not found:
            if find_string in lines[counter]:
                found = True
            counter += 1
        return found
    
    def similar_line(before_line, after_line, percentage_similar = 0.4):
        before_words = UtilityText.generate_words(before_line)
        after_words = UtilityText.generate_words(after_line)
        before_counter = 0
        number_found = 0
        similar = False
        if len(before_words) > 0:
            while number_found/len(before_words) < percentage_similar and before_counter < len(before_words):
                if before_words[before_counter] in after_words:
                    number_found += 1
                before_counter += 1
            if number_found/len(before_words) >= percentage_similar:
                similar = True
        return similar

    def remove_zero_length_words(initial_words):
        words = []
        for word in initial_words:
            if len(word) > 0:
                words.append(word)
        return words
    
    def string_find_from(input_string, find_string):
        output_string = ""
        if find_string in input_string:
            output_string = input_string[input_string.find(find_string) + len(find_string):]
        return output_string

    def string_find_from_to(input_string, find_string, to_patterns):
        output_string = UtilityText.string_find_from(input_string, find_string)
        first_ocurence = UtilityText.first_occurence(output_string, to_patterns)
        return output_string[0:first_ocurence]

    def formate_text(input_text):
        if input_text is None:
            output = ""
        else:
            output = input_text.replace("'", "''")
            output = output.replace("\n", "")
        return output

    def first_occurence(input_string, to_patterns):
        minimum_position = len(input_string)
        for pattern in to_patterns:
            pattern_position = input_string.find(pattern)
            if pattern_position > 0 and pattern_position < minimum_position:
                minimum_position = pattern_position
        return minimum_position

    def leading_zero(number):
        return "{:02d}".format(number)
if __name__ == "__main__":
    utility_text = UtilityText()
    list = ["testPlayToHandAtTableCanPlayASevenPass", "testPlayToHandAtTableCanPlayASevenFail", "testPlayToHandAtTablePlayASeven", "testPlayToHandAtTableCanPlayASixPass", "testPlayToHandAtTableCanPlayAFiveFail", "testPlayToHandAtTablePlayASix"]
    for word in list:
        print(utility_text.change_camel_case_to_snake(word))
