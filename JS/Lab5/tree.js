class Tree {
  root = new TreeNode();
  constructor() {}
  setRoot(root) {
    this.root = root;
  }
  print() {
    this.root.map(node=>console.log(node))
  }
}

class TreeNode {
  value;
  constructor(value) {
    this.value = value;
  }
  putLeft(leftNode) {
    this.leftNode = leftNode;
  }
  putRight(rightNode) {
    this.rightNode = rightNode;
  }
  getLeft() {
    return this.leftNode;
  }
  getRight() {
    return this.rightNode;
  }
}

const myTree = new Tree();
const rootNode = new TreeNode(22);

rootNode.putLeft(new TreeNode(11));
rootNode.putRight(new TreeNode(12));

rootNode.getLeft().putLeft(new TreeNode(10));
rootNode.getRight().putRight(13);

myTree.setRoot(rootNode);

myTree.print();
