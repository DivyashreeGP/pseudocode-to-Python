import re

class SDTTranslator:
    def __init__(self):
        self.code = []  # Stores the translated Python code
        self.indent_level = 0  # Tracks current indentation level

    def translate_algorithm(self, algorithm_lines):
        """Translate a list of algorithm lines into Python code."""
        self.code = []  # Reset code
        self.indent_level = 0  # Reset indentation

        for line in algorithm_lines:
            self.process_line(line.strip())  # Process each line

        # Add a final newline after all test cases
        self.code.append("")  
        return "\n".join(self.code)

    def process_line(self, line):
        """Process each line and apply SDT rules."""
        if line.startswith("#"):  # Skip comments
            return

        if line.startswith("Initialize"):
            self.handle_initialization(line)
        elif line.startswith("Function"):
            self.handle_function_definition(line)
        elif line.startswith("For"):
            self.handle_for_loop(line)
        elif line.startswith("While"):
            self.handle_while_loop(line)
        elif line.startswith("DoWhile"):
            self.handle_do_while_loop(line)
        elif line.startswith("If"):
            self.handle_if_condition(line)
        elif line.startswith("Elif"):
            self.handle_elif_condition(line)
        elif line.startswith("Else"):
            self.handle_else(line)
        elif line.startswith("Return"):
            self.handle_return(line)
        elif line.startswith("Print"):
            self.handle_print(line)
        elif line.startswith("Insert"):
            self.handle_insert_into_array(line)
        elif line.startswith("Remove"):
            self.handle_remove_from_array(line)
        elif line.startswith("Access"):
            self.handle_access_array(line)
        elif line.startswith("Update"):
            self.handle_update_array(line)
        elif line.startswith("Find"):
            self.handle_find_length(line)
        elif line.startswith("Sort"):
            self.handle_sort_array(line)
        elif line.startswith("Reverse"):
            self.handle_reverse_array(line)
        elif line.startswith("Push"):
            self.handle_stack_push(line)
        elif line.startswith("Pop"):
            self.handle_stack_pop(line)
        elif line.startswith("Peek"):
            self.handle_stack_peek(line)
        elif line.startswith("Enqueue"):
            self.handle_enqueue(line)
        elif line.startswith("Dequeue"):
            self.handle_dequeue(line)
        elif re.search(r"(\+|-|\*|/|%)", line):  # Detect arithmetic operations
            self.handle_arithmetic(line)
        elif "=" in line:  # Handle general assignments
            self.handle_assignment(line)
        elif line.startswith("End"):
            self.indent_level -= 1  # End of a block reduces indentation
        else:
            self.code.append(self.get_indent() + f"")

    # Handlers for Operations
    def handle_initialization(self, line):
        """Handle initialization statements."""
        # Example: "Initialize result to 1"
        parts = line.split("to")
        var = parts[0].replace("Initialize", "").strip()
        value = parts[1].strip()
        self.code.append(self.get_indent() + f"{var} = {value}")
    def handle_function_definition(self, line):
        """Handle function definitions with or without parameters."""
        line = line.replace("Function", "").strip()
        if not line.endswith(":"):
            self.code.append(self.get_indent() + f"# Invalid function definition syntax: {line}")
            return
        self.code.append(self.get_indent() + f"def {line}")
        self.indent_level += 1

    def handle_for_loop(self, line):
        """Handle for loop statements."""
        # Example: "For i from 1 to n:"
        line = line.rstrip(":")  # Remove the trailing colon if present
        parts = line.split("from")
        loop_var = parts[0].replace("For", "").strip()
        range_parts = parts[1].split("to")
        start = range_parts[0].strip()
        end = range_parts[1].strip()
        self.code.append(self.get_indent() + f"for {loop_var} in range({start}, {end} + 1):")
        self.indent_level += 1

    def handle_while_loop(self, line):
        """Handle while loops."""
        condition = line.replace("While", "").strip()
        self.code.append(self.get_indent() + f"while {condition}:")
        self.indent_level += 1

    def handle_do_while_loop(self, line):
        """Handle do-while loops."""
        self.code.append(self.get_indent() + "while True:  # Do-while loop")
        self.indent_level += 1

    def handle_if_condition(self, line):
        """Handle if conditions."""
        condition = line.replace("If", "").strip()
        self.code.append(self.get_indent() + f"if {condition}:")
        self.indent_level += 1

    def handle_elif_condition(self, line):
        """Handle elif conditions."""
        condition = line.replace("Elif", "").strip()
        self.code.append(self.get_indent() + f"elif {condition}:")
        self.indent_level += 1

    def handle_else(self, line):
        """Handle else conditions."""
        self.code.append(self.get_indent() + "else:")
        self.indent_level += 1

    def handle_return(self, line):
        """Handle return statements."""
        value = line.replace("Return", "").strip()
        self.code.append(self.get_indent() + f"return {value}")

    def handle_print(self, line):
        """Handle print statements."""
        value = line.replace("Print", "").strip()
        self.code.append(self.get_indent() + f"print({value})")

    def handle_insert_into_array(self, line):
        """Handle array insertion."""
        match = re.match(r"Insert (.+) into (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid insertion syntax: {line}")
            return
        value, array = match.groups()
        self.code.append(self.get_indent() + f"{array}.append({value})")

    def handle_remove_from_array(self, line):
        """Handle array removal."""
        match = re.match(r"Remove (.+) from (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid removal syntax: {line}")
            return
        value, array = match.groups()
        self.code.append(self.get_indent() + f"{array}.remove({value})")

    def handle_update_array(self, line):
        """Handle array element update."""
        match = re.match(r"Update (.+)\[(.+)\] to (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid update syntax: {line}")
            return
        array, index, value = match.groups()
        self.code.append(self.get_indent() + f"{array}[{index}] = {value}")

    def handle_access_array(self, line):
        """Handle array access."""
        match = re.match(r"Access (.+)\[(.+)\]", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid access syntax: {line}")
            return
        array, index = match.groups()
        self.code.append(self.get_indent() + f"{array}[{index}]")

    def handle_find_length(self, line):
        """Handle finding array length."""
        match = re.match(r"Find length of (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid find length syntax: {line}")
            return
        array = match.groups()[0]
        self.code.append(self.get_indent() + f"len({array})")

    def handle_sort_array(self, line):
        """Handle sorting the array."""
        match = re.match(r"Sort (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid sort syntax: {line}")
            return
        array = match.groups()[0]
        self.code.append(self.get_indent() + f"{array}.sort()")

    def handle_reverse_array(self, line):
        """Handle reversing the array."""
        match = re.match(r"Reverse (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid reverse syntax: {line}")
            return
        array = match.groups()[0]
        self.code.append(self.get_indent() + f"{array}.reverse()")

    def handle_stack_push(self, line):
        """Handle stack push."""
        match = re.match(r"Push (.+) to (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid stack push syntax: {line}")
            return
        value, stack = match.groups()
        self.code.append(self.get_indent() + f"{stack}.append({value})")

    def handle_stack_pop(self, line):
        """Handle stack pop."""
        match = re.match(r"Pop from (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid stack pop syntax: {line}")
            return
        stack = match.groups()[0]
        self.code.append(self.get_indent() + f"{stack}.pop()")

    def handle_stack_peek(self, line):
        """Handle stack peek."""
        match = re.match(r"Peek (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid stack peek syntax: {line}")
            return
        stack = match.groups()[0]
        self.code.append(self.get_indent() + f"{stack}[-1]")

    def handle_enqueue(self, line):
        """Handle enqueue."""
        match = re.match(r"Enqueue (.+) to (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid enqueue syntax: {line}")
            return
        value, queue = match.groups()
        self.code.append(self.get_indent() + f"{queue}.append({value})")

    def handle_dequeue(self, line):
        """Handle dequeue."""
        match = re.match(r"Dequeue from (.+)", line)
        if not match:
            self.code.append(self.get_indent() + f"# Invalid dequeue syntax: {line}")
            return
        queue = match.groups()[0]
        self.code.append(self.get_indent() + f"{queue}.pop(0)")

    def handle_arithmetic(self, line):
        """Handle arithmetic operations."""
        self.code.append(self.get_indent() + line)

    def handle_assignment(self, line):
        """Handle assignment statements."""
        self.code.append(self.get_indent() + line)

    def get_indent(self):
        """Get the current indentation level."""
        return "    " * self.indent_level
