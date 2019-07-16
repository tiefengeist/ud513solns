def three_sum(nums)
#     return [] if nums.size < 3

#     return [[0,0,0]] if nums.uniq == [0]

#     res = []

#     nums.sort!

#     (1..nums.size-2).step(1) do |m|
#         l = m - 1
#         r = m + 1

#         while(l >= 0 && r < nums.size)
#             sum = [nums[l], nums[m], nums[r]].sum

#             case
#                 when sum == 0
#                 then
#                     res << [nums[l], nums[m], nums[r]]
#                     l = l -1
#                 when sum > 0 then l = l - 1
#                 when sum < 0 then r = r + 1
#                 end
#         end
#     end
#     return res.uniq

    sums = []
    nums.sort!

    for i in 0..(nums.length - 3)
        next if i > 0 && nums[i - 1] == nums[i]
        j = i + 1
        k = nums.length - 1
        while (j < k) do
            sum = nums[i] + nums[j] + nums[k]
            if sum > 0
                k -= 1
            elsif sum < 0
                j += 1
            else
                sums << [nums[i], nums[j], nums[k]]
                j += 1
                k -= 1
                j += 1 while nums[j] == nums[j - 1]
                k -= 1 while nums[k] == nums[k + 1]
            end
        end
    end

    return sums
end
