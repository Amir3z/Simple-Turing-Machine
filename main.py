from turing_machine import TuringMachine

transitions = {}
with open("./input.txt", "r") as file:
    lines = file.readlines()
    states = int(lines[0].strip())
    transitions_count = int(lines[1].strip())
    accepting_state = int(lines[2].strip())
    rejecting_state = int(lines[3].strip())

    for line in lines[4:]:
        current_state, next_state, read_symbol, write_symbol, move_direction = (
            line.strip().split()
        )
        transitions[(int(current_state), read_symbol)] = (
            int(next_state),
            write_symbol,
            move_direction,
        )

    file.close()

input_string = input("TM Input: ")

# Display parsed data
print("Number of States:", states)
print("Number of Edges:", transitions_count)
print("Accepting State:", accepting_state)
print("Rejecting State:", rejecting_state)
print("Transitions:", transitions)
print("input:", input_string)

# Process the parsed data
tm = TuringMachine(states, accepting_state, rejecting_state, transitions)
tm.load_tape(input_string)
result = tm.run()
print("Result:", result)
