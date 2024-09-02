def and_gate(and_gate_input, number_of_inputs):
    and_output = and_gate_input[0]
    for i in range(number_of_inputs):
        and_output = and_output * gate_input[i]
    return and_output

def or_gate(or_gate_input, number_of_inputs):
    or_output = or_gate_input[0]
    for i in range(number_of_inputs):
        if or_gate_input[i] == 1:
            or_output = 1
        else:
            or_output = or_output
    return or_output

def not_gate(not_gate_input):
    if not_gate_input == 1:
        not_output = 0
    else:
        not_output = 1
    return not_output

def nand_gate(nand_gate_input, number_of_inputs):
    pass

gate_input = [1, 0]
output = or_gate(or_gate_input=gate_input, number_of_inputs=2)
print(output)
