def and_gate(and_gate_input, number_of_inputs):
    and_output = and_gate_input[0]
    for i in range(1, number_of_inputs):
        and_output = and_output * gate_input[i]
    return and_output

def or_gate(or_gate_input, number_of_inputs):
    or_output = or_gate_input[0]
    for i in range(1, number_of_inputs):
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
    nand_output = and_gate(nand_gate_input, number_of_inputs)
    nand_output = not_gate(nand_output)
    return nand_output

def nor_gate(nor_gate_input, number_of_inputs):
    nor_output = or_gate(nor_gate_input, number_of_inputs)
    nor_output = not_gate(nor_output)
    return nor_output

def xor_gate(xor_gate_input, number_of_inputs):
    xor_output = xor_gate_input[0]
    for i in range(1, number_of_inputs):
        if xor_output == xor_gate_input[i]:
            xor_output = 0
        else:
            xor_output = 1
    return xor_output

def xnor_gate(xnor_gate_input, number_of_inputs):
    xnor_output = xor_gate(xnor_gate_input, number_of_inputs)
    xnor_output  = not_gate(xnor_output)
    return xnor_output

if __name__ == "__main__":
    gate_input = [1, 0]
    output = xnor_gate(gate_input, number_of_inputs=2)
    print(output)
