def reverse(x)
    # digits = x.digits
    # f = 0
    # l = digits.length - 1
    # while l > f
    #     digits[f] = digits[l]
    #     f += 1
    #     l -= 1
    # end
    # digits.join

    result = x.to_s.split("").reverse.join("").to_i
    result *= -1 if x < 0
    return 0 if result > 2**31 - 1 || result < -2**31
else return result
end
