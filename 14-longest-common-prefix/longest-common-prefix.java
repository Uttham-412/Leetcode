class Solution {
    public String longestCommonPrefix(String[] strs) {

        // Take the first string as reference
        String first = strs[0];

        // Check each character of the first string
        for (int i = 0; i < first.length(); i++) {

            char currentChar = first.charAt(i);

            // Compare this character with every other string
            for (int j = 1; j < strs.length; j++) {

                // If current string is shorter
                // or characters don't match
                if (i == strs[j].length() || strs[j].charAt(i) != currentChar) {

                    // Return prefix found so far
                    return first.substring(0, i);
                }
            }
        }

        // Entire first string is common
        return first;
    }
}