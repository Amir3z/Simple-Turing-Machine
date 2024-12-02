class TuringMachine:
    def __init__(self, states, accepting_state, rejecting_state, transitions):
        self.states = list(range(0, states))
        self.accepting_state = accepting_state
        self.rejecting_state = rejecting_state
        self.transitions = transitions
        self.head = 0
        self.current_state = 0
        self.tape = ["*"]

    def print_config(self):
        left_part = "".join(self.tape[: self.head])  # Tape to the left of the head
        right_part = "".join(
            self.tape[self.head :]
        )  # Tape including and to the right of the head
        conf = f"{left_part}<q{self.current_state}>{right_part}"
        print(conf)

    def load_tape(self, input_string):
        self.tape = list(input_string) + ["*"]
        self.head = 0
        self.current_state = 0

    def step(self):
        current_symbol = self.tape[self.head]
        transition_key = (self.current_state, current_symbol)

        if transition_key not in self.transitions:
            self.current_state = self.rejecting_state
            return
            # or raise Exception(f"No transition was found for {transition_key}")
        if len(self.tape) == 0:
            raise ValueError("Input tape is empty!")

        next_state, write_symbol, move_direction = self.transitions[transition_key]
        self.print_config()

        self.tape[self.head] = write_symbol
        self.current_state = next_state

        if move_direction == "R":
            self.head += 1
            if self.head >= len(self.tape):
                self.tape.append("*")
        elif move_direction == "L":
            if self.head > 0:
                self.head -= 1
            else:
                self.tape.insert(0, "*")

    def run(self):
        special_states = [self.accepting_state, self.rejecting_state]
        while self.current_state not in special_states:
            self.step()
        self.print_config()
        return "Accepted" if self.current_state == self.accepting_state else "Rejected"
