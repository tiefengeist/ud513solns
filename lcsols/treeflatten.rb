def flatten(root)

    current = root

    # Loop through the tree
    while current != nil do
        # if there is a left subtree
       if current.left != nil
           new = current.left
           # Iterate to the end of the right subtree
           while new.right != nil do
              new = new.right
           end
           # Draw a picture to understand it
           new.right = current.right
           current.right = current.left
           current.left = nil
       end
       current = current.right
    end
end
