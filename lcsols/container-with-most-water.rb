def max_area(height)
    l = 0
    r = height.length - 1
    max = 0
    while r > l
        area = (r-l) * [height[r], height[l]].min
        max = area if area > max
        if height[l] < height[r]
            l += 1
        else
            r -= 1
        end
    end
    max
end
