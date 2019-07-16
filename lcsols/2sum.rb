def two_sum(nums, target)
    search = {}
    nums.each_with_index do |num,i|
      return [search[target-num], i] unless search[target-num].nil?
      search[num] = i
    end
end
