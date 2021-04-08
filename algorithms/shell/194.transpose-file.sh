#
# @lc app=leetcode id=194 lang=bash
#
# [194] Transpose File
#

# @lc code=start
# Read from the file file.txt and print its transposed content to stdout.

function using_awk_1() {
    awk '{
        for (i=1;i<=NF;i++){
            if (NR==1){
                output[i]=$i
            } else {
                output[i]=output[i]" "$i
            }
        }
    } END {
        for (i=1;i<=NF;i++){
            print output[i]
        }
    }' file.txt
}

function using_awk_2() {
    awk '{
        for (i=1;i<=NF;i++){
            output[i]=output[i] FS $i
        }
    } END {
        for (i=1;i<=NF;i++){
            print output[i]
        }
    }' file.txt | sed 's/^ //g'
}

# using_awk_1
using_awk_2

# @lc code=end
