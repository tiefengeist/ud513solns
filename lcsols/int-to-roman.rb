def int_to_roman(int)
  roman_numerals = {
      1000 => "M",
       900 => "CM",
       500 => "D",
       400 => "CD",
       100 => "C",
        90 => "XC",
        50 => "L",
        40 => "XL",
        10 => "X",
         9 => "IX",
         5 => "V",
         4 => "IV",
         1 => "I",
  }
  raise ArgumentError, "Input int has to be an Integer" unless int.is_a?(Integer)
  raise ArgumentError, "Input int can only be in the range 1 - 3999" unless int >= 1 && int <= 3999
  return 'nulla' if int == 0
  roman = ""
  roman_numerals.each do |value, letter|
    roman << letter * (int / value)
    int = int % value
  end
  return roman
end
