def bin_sum(bin1, bin2):
    if len(bin2) > len(bin1):
        bin1, bin2 = bin2, bin1

    carry = 0
    b1_index = len(bin1) - 1
    b2_index = len(bin2) - 1

    result = []
    while b1_index >= 0:
        sum_ = 0
        sum_ += int(bin1[b1_index])
        sum_ += int(bin2[b2_index]) if b2_index >= 0 else 0
        sum_ += carry
        result.append("0") if sum_ % 2 == 0 else result.append("1")
        carry = 1 if sum_ > 1 else 0

        b1_index -= 1
        b2_index -= 1

    if carry == 1:
        result.append("1")

    return "".join(result[::-1])


if __name__ == "__main__":
    b1 = input()
    b2 = input()
    print(bin_sum(b1, b2))

