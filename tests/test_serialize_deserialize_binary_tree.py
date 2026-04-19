import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solutions'))

from serialize_deserialize_binary_tree import TreeNode, Codec


def build_tree(values):
    """Helper: build a tree from a list (BFS order, None = missing node)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def trees_are_equal(a, b):
    """Helper: check two trees have the same structure and values."""
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and trees_are_equal(a.left, b.left) and trees_are_equal(a.right, b.right)


codec = Codec()


def test_normal_tree():
    """A standard tree with left and right children serializes and deserializes correctly."""
    original = build_tree([1, 2, 3, None, None, 4, 5])
    result = codec.deserialize(codec.serialize(original))
    assert trees_are_equal(original, result)


def test_empty_tree():
    """An empty tree (None) serializes to a string and deserializes back to None."""
    result = codec.deserialize(codec.serialize(None))
    assert result is None


def test_single_node():
    """A tree with just one node roundtrips correctly."""
    original = TreeNode(42)
    result = codec.deserialize(codec.serialize(original))
    assert trees_are_equal(original, result)


def test_left_skewed_tree():
    """A tree where every node only has a left child works correctly."""
    original = build_tree([1, 2, None, 3, None])
    result = codec.deserialize(codec.serialize(original))
    assert trees_are_equal(original, result)


def test_right_skewed_tree():
    """A tree where every node only has a right child works correctly."""
    original = build_tree([1, None, 2, None, 3])
    result = codec.deserialize(codec.serialize(original))
    assert trees_are_equal(original, result)


def test_negative_values():
    """Trees with negative node values are handled correctly."""
    original = build_tree([-1, -2, -3])
    result = codec.deserialize(codec.serialize(original))
    assert trees_are_equal(original, result)
