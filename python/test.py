'''
last method first hw

    minVal = min(nums)
    maxVal = max(nums)

    cntMin = nums.count(minVal)
    cntMax = nums.count(maxVal)

    if cntMin > 1 and cntMax > 1:
        return ((sum(nums) - ((cntMin-1)*minVal) - ((cntMax-1)*maxVal)) // (len(nums)-(cntMin-1)-(cntMax-1)))

    elif cntMin == 1 and cntMax > 1:
        return ((sum(nums) - ((cntMax-1) * maxVal) - minVal) // (len(nums) - (cntMax-1) - 1))
    
    elif cntMin > 1 and cntMax == 1:
        return ((sum(nums) - ((cntMin-1) * minVal) - maxVal) // (len(nums) - (cntMin-1) - 1))

    else: #if max and min only appear once
        return ((sum(nums) - minVal - maxVal ) // (len(nums)-2))
'''