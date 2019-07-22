def postorder_traversal(root)
    ans = []
    def traverse(node, ans)
        if node != nil
            traverse(node.left, ans)
            traverse(node.right,ans)
            ans.push(node.val)
        end
    end
    traverse(root,ans)
    return ans
end
