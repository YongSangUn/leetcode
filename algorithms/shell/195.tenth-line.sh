#
# @lc app=leetcode id=195 lang=bash
#
# [195] Tenth Line
#

# @lc code=start
# Read from the file file.txt and output the tenth line to stdout.

function using_sed() {
    sed -n '10 p' file.txt
}

function using_awk() {
    awk 'NR==10' file.txt
}

using_sed

# @lc code=end
