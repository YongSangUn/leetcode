#
# @lc app=leetcode id=193 lang=bash
#
# [193] Valid Phone Numbers
#

# @lc code=start
# Read from the file file.txt and output all valid phone numbers to stdout.

function using_awk() {
    awk '/^([0-9]{3}-){2}[0-9]{4}$/ || /^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$/' file.txt
}

function using_grep() {
    grep -E '^([0-9]{3}-){2}[0-9]{4}$|^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$' file.txt
}

using_grep
# @lc code=end
