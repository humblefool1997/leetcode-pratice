class Solution:
    def longestUniqueSubsttr(self, S):
        str = ""
        str = S
        
    # list to mark characters present in the current window
        window = {}
 
    # stores the longest substring boundaries
        begin = end = 0
 
    # `[low…high]` maintain the sliding window boundaries
        low = high = 0
 
        while high < len(str):
 
        # if the current character is present in the current window
            if window.get(str[high]):
 
            # remove characters from the left of the window till
            # we encounter the current character
                while str[low] != str[high]:
                    window[str[low]] = False
                    low = low + 1
 
                low = low + 1        # remove the current character
            else:
            # if the current character is not present in the current
            # window, include it
                window[str[high]] = True
 
            # update the maximum window size if necessary
               if end - begin < high - low:
                begin = low
                end = high
 
            high = high + 1
 
    # return the longest substring found at `str[begin…end]`
        return str[begin:end + 1]