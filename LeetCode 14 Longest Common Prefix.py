"""
Author: Isaac Asante
YouTube tutorials: https://www.youtube.com/@nextrie
Website: https://isaacasante.com/
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Start from the root
        node = self.root

        # Iterate through characters
        for char in word:
            # Is the character a child of the current node?
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node
            node = node.children[char]
        # Mark the end of the processed word
        node.isWord = True


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        prefix = ""
        node = trie.root

        # Add every word into the Trie
        for word in strs:
            trie.insert(word)

        while True:
            """Follow the path where there's only one child node, until many child nodes have been found, as that path corresponds to the same initial characters in every word. Encountering a full word completes the prefix search."""
            if len(node.children) == 1 and not node.isWord:
                # The key is the character, the value is the TrieNode object.
                char, next_node = next(iter(node.children.items()))
                # Update the prefix
                prefix += char
                node = next_node
            else:
                break

        return prefix
