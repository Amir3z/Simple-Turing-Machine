# Turing Machine Simulator

This project simulates a very basic Turing Machine. It accepts an input tape, processes it based on a set of states and transitions, and determines whether the input is **accepted** or **rejected**.

## How It Works

A **Turing Machine** consists of:

1. A finite set of states.
2. A tape divided into cells, that the machine can read and write.
3. A head that moves left or right on the tape.
4. Transitions that define what to do in each state.

The machine starts at the initial state with the head at the beginning of the tape. It processes the input based on transitions until it reaches either:

- The **accepting state**.
- The **rejecting state**.

## Input Format

The program expects a text file (`input.txt`) with the following format:

1. **Line 1:** Number of states.
2. **Line 2:** Number of transitions.
3. **Line 3:** ID of the accepting state.
4. **Line 4:** ID of the rejecting state.
5. **Lines 5+:** Transitions in the format:
   <current_state> <next_state> <read_symbol> <write_symbol> <move_direction>

### Example Input File

```
7
15
5
6
0 1 0 * R
0 6 * * R
0 6 X * R
1 1 X * R
1 2 0 X R
1 5 * * R
2 4 * * L
2 2 X * R
2 3 0 * R
3 2 0 X R
3 3 X * R
3 6 * * R
4 4 0 * L
4 4 X * L
4 1 * * R
```

## Running the Program

1. **Setup Input File:** Ensure the `input.txt` file contains the machine's definition and transitions as described above.
2. **Run the Program:** Execute the script using Python:
   ```bash
   python main.py
   ```
3. **Provide Input Tape**: When prompted, enter the input tape as a string (e.g., 010).

## Output

The program outputs:

1. Parsed details of the Turing Machine (states, transitions, etc.).
2. Each step's configuration:
   `<left_tape><q<current_state>><right_tape>`
3. Final result: **Accepted**, **Rejected**, or an **error** if the input is invalid.

## Notes

1. If no valid transition exists for the current state and symbol, the machine transitions to the **rejecting** state.
2. The program halts if the machine reaches the **accepting** or **rejecting** state.
3. Ensure the input tape and transitions are formatted correctly to avoid runtime errors.
4. Blank space is presented by '\*'
