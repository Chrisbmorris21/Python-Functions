from datetime import date

example_data_set = ['Data Value', ['Data Value', (1, 2, 3,), ['a', 'b']]]
refined_data_set = []
types_list = [str, int, date]


def break_down_list(value):

    def break_down_list_more(semi_refined_data):
        for record in semi_refined_data:
            break_down_list(record)
        return value

    def append_list(refined_data):
        if refined_data is not None:
            record_entry = (len(refined_data_set), refined_data)
        refined_data_set.append(record_entry)
        return value

    if type(value) in types_list:
        append_list(value)
    else:
        break_down_list_more(value)


break_down_list(example_data_set)
for item in refined_data_set:
    print(item[1])
