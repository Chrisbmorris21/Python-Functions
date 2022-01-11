from datetime import date

types_list = [str, int, date]
example_data_set = ['Data Value', ['Data Value', (1, 2, 3,), ['a', 'b']]]
refined_data_set = []


def flatten_data_to_array(value):
    # Receives raw data type and condenses all values into a single 2d array with key:value pairs

    def break_down_list(value_a):
        # Receives raw data
        for semi_refined_data in value_a:
            flatten_data_to_array(semi_refined_data)
        return value_a

    def append_list(value_b):

        if value_b is not None:
            record_entry = (len(refined_data_set), value_b)
            refined_data_set.append(record_entry)
        return value_b

    if type(value) in types_list:
        append_list(value)
    else:
        break_down_list(value)

    for record in refined_data_set:
        print(record[1])


flatten_data_to_array(example_data_set)
