from ComponentsLogic import xor_gate
truth_table = {1, 0, 1, 1}
max_bits = 6

def binary(input_num):
    min_bits = int(input_num/2)
    num_representation = [0]*max_bits
    for i in range(min_bits, -1, -1):
        bit = int(input_num / pow(2, i))
        input_num %= pow(2, i)
        if bit == 1:
            num_representation[i] = 1
    return num_representation

def gray_code(input_num):
    binary_num = binary(input_num)
    min_bits = int(input_num/2)
    gray_code_output = [0]*max_bits
    gray_code_output[min_bits] = binary_num[min_bits]
    for i in range(min_bits-1, -1, -1):
        xor_input = [binary_num[i], binary_num[i+1]]
        gray_code_output[i] = xor_gate(xor_input)
    return gray_code_output


test_case = gray_code(2)
print(test_case)