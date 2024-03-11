action_table = {0: {"id":"shift_5", "(": "shift_4"}, 1:{"+":"shift_6", "$": "accept_0"}, 2: {"+": "reduce_2", "*": "shift_7", ")": "reduce_2", "$": "reduce_2"},
                3: {"+": "reduce_4", "*": "reduce_4", ")": "reduce_4", "$": "reduce_4"}, 4: {"id": "shift_5", "(": "shift_4"}, 5: {"+": "reduce_6", "*": "reduce_6", ")": "reduce_6", "$": "reduce_6"},
                6: {"id": "shift_5", "(": "shift_4"}, 7: {"id": "shift_5", "(": "shift_4"}, 8: {"+": "shift_6", ")": "shift_11"}, 9: {"+": "reduce_1", "*": "shift_7", ")": "reduce_1", "$": "reduce_1"},
                10: {"+": "reduce_3", "*": "reduce_3", ")": "reduce_3", "$": "reduce_3"}, 11: {"+": "reduce_5", "*": "reduce_5", ")": "reduce_5", "$": "reduce_5"}}

process_stack = [0]
input_queue_str = input("Enter your string: ")
input_queue = []

for i in range(len(input_queue_str)):
    char = input_queue_str[i]
    if char in "()+*id":
        if char in "()+*":
            input_queue.append(char)
        elif char == 'i' and input_queue_str[i + 1] == 'd':
            input_queue.append('id')
        elif char == 'd' and input_queue_str[i - 1] == 'i':
            continue
        else:
            print("INVALID string entered. SYNTAX ERROR!")
            exit()

    else:
        print("INVALID string entered. SYNTAX ERROR!")
        exit()
        
input_queue.append('$')
            

def shift(next_line):
    global process_stack
    global input_queue
    if len(input_queue) > 0:
        queue_element = input_queue.pop(0)
        process_stack.append(queue_element)
        process_stack.append(next_line) 
    else:
        print("INVALID string entered. SYNTAX ERROR!")
        exit()

def go_to():
    go_to_table = {"E": {0: 1, 4: 8}, "T": {0: 2, 4: 2, 6: 9}, "F": {0: 3, 4: 3, 6: 3, 7: 10}}
    global process_stack
    try:
        state, letter = int(process_stack[-2]), process_stack[-1]
    except ValueError:
        return -1
    
    push_str = str(go_to_table[letter][state])
    
    process_stack.append(push_str)
    return 0

def reduce(case):
    global process_stack

    found_str = ""
    target_str = ""
    push_str = ""
    case = int(case)

    if case == 1:
        target_str = "E+T"
        push_str = "E"
    elif case == 2:
        target_str = "T"
        push_str = "E"
    elif case == 3:
        target_str = "T*F"
        push_str = "T"
    elif case == 4:
        target_str = "F"
        push_str = "T"
    elif case == 5:
        target_str = "(E)"
        push_str = "F"
    else:
        target_str = "id"
        push_str = "F"

    while (found_str != target_str):
        candidate_element = str(process_stack.pop(-1))
        if not candidate_element.isnumeric():
            found_str = candidate_element + found_str

        if len(process_stack) < 1:
            print("INVALID string entered. SYNTAX ERROR!")
            exit()
    process_stack.append(push_str)
    if go_to() == -1:
        print("INVALID string entered. SYNTAX ERROR!")
        exit()
    

while len(input_queue) > 0:
    status = process_stack[-1]
    try:
        action_and_state = action_table[int(status)][str(input_queue[0])].split('_')
    except KeyError:
        print("INVALID string entered. SYNTAX ERROR!")
        exit()
    action, action_state = action_and_state[0], action_and_state[1]
    if action == "accept":
        print("VALID string entered. ACCEPTED!")
        exit(0)
    elif action == "shift":
        shift(action_state)
    else:
        reduce(action_state)
print("INVALID string entered. SYNTAX ERROR!")
