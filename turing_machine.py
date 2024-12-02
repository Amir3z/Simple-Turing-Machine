class TuringMachine:
    def __init__(self, states, accepting_state, rejecting_state, transitions):
        """Initializes the Turing Machine.

        Args:
            states (int): Total number of states.
            accepting_state (int): ID of the accepting state.
            rejecting_state (int): ID of the rejecting state.
            transitions (dict): Dictionary representing state transitions.
        """

        self.states = list(range(0, states))
        self.accepting_state = accepting_state
        self.rejecting_state = rejecting_state
        self.transitions = transitions
        self.head = 0
        self.current_state = 0
        self.tape = ["*"]

    def print_config(self):
        """Prints the current configuration of the Turing Machine."""

        left_part = "".join(self.tape[: self.head])  # Tape to the left of the head
        right_part = "".join(
            self.tape[self.head :]
        )  # Tape including and to the right of the head
        conf = f"{left_part}<q{self.current_state}>{right_part}"
        print(conf)

    def load_tape(self, input_string):
        """Loads an input string onto the tape.

        Args:
            input_string (str): The input string to be processed.
        """

        self.tape = list(input_string) + ["*"]
        self.head = 0
        self.current_state = 0

    def step(self):
        """Executes a single step of the Turing Machine.

        Raises:
            ValueError: If the input tape is empty.
        """

        if len(self.tape) == 0:
            raise ValueError("Input tape cannot be empty!")

        current_symbol = self.tape[self.head]
        transition_key = (self.current_state, current_symbol)

        if transition_key not in self.transitions:
            print(
                f"No transition found for {transition_key}. Moving to rejecting state."
            )
            self.current_state = self.rejecting_state
            return
            # or just raise Exception(f"No transition was found for {transition_key}")

        next_state, write_symbol, move_direction = self.transitions[transition_key]
        self.print_config()

        self.tape[self.head] = write_symbol
        self.current_state = next_state

        # moving the head on tape
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
        """Runs and processes the tape with the Turing Machine and returns the result

        Returns:
            str: Accepted/Rejected/Loop
        """
        special_states = [self.accepting_state, self.rejecting_state]
        steps = 0
        max_steps = 1000

        while self.current_state not in special_states:
            self.step()
            steps += 1

            if steps >= max_steps:
                return "Loop detected"

        self.print_config()  # The last config
        return "Accepted" if self.current_state == self.accepting_state else "Rejected"
