public class BinarySearchTree {
	private BinarySearchTreeNode root;

	public BinarySearchTree() {
		root = null;
	}

	public BinarySearchTree(int data) {
		root = new BinarySearchTreeNode(data);
	}

	public void add(int data) {
		if (root == null) root = new BinarySearchTreeNode(data);
		else root.add(data);
	}

	public void delete(int data) {
		if (root == null || root.search(data) == null) return;
		root = root.delete(data);
	}

	public BinarySearchTreeNode search(int data) {
		return (root == null) ? null : root.search(data);
	}

	public void printTree() {
		System.out.print("[");
		if (root == null) System.out.print("null");
		else root.printTree();
		System.out.print("]\n");
	}
}


class BinarySearchTreeNode {
	private final int DATA;
	private BinarySearchTreeNode left, right;

	BinarySearchTreeNode(int data) {
		this.DATA = data;
		this.left = null;
		this.right = null;
	}

	void add(int data) {
		if (this.DATA < data) {
			if (right != null) right.add(data);
			else right = new BinarySearchTreeNode(data);
		} else {
			if (left != null) left.add(data);
			else left = new BinarySearchTreeNode(data);
		}
	}

	BinarySearchTreeNode delete(int data) {
		// under construction
	}

	BinarySearchTreeNode search(int data) {
		if (this.DATA == data) return this;
		if (this.DATA < data) return (right == null) ? null : right.search(data);
		else return (left == null) ? null : left.search(data);
	}

	void printTree() {
		if (left != null) left.printTree();
		System.out.print(" " + DATA);
		if (right != null) right.printTree();
	}
}
