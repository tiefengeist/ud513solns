def longest_common_prefix(strs)
    if strs.empty?
        return ""
    end
    s = ""
    init = strs[0]
    for i in 0..init.length-1
        if strs.all?{|x| x[i] == init[i]}
            s += init[i]
        else
            break
        end
    end
    s
end
