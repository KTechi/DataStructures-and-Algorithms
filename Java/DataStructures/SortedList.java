public class SortedList {
	private SortedListNode head;

	public SortedList() {
		head = null;
	}

	public SortedList(int data) {
		head = new SortedListNode(data, null);
	}

	public void insert(int data) {
		if (head == null) head = new SortedListNode(data, null);
		else if (data < head.getValue()) head = new SortedListNode(data, head);
		else head.insert(data);
	}

	public boolean delete(int data) {
		if (head == null) return false;
		if (head.getValue() == data) {
			head = head.getNext();
			return true;
		}
		return head.delete(data);
	}

	public SortedListNode search(int data) {
		return (head == null) ? null : head.search(data);
	}

	public void printList() {
		if (head == null) System.out.println("[null]");
		else {
			System.out.print("[" + head.getValue());
			head.printList();
			System.out.print("]\n");
		}
	}
}


class SortedListNode {
	private final int DATA;
	private SortedListNode next;

	SortedListNode(int data, SortedListNode next) {
		this.DATA = data;
		this.next = next;
	}

	int getValue() {
		return DATA;
	}

	SortedListNode getNext() {
		return next;
	}

	void insert(int data) {
		if (next == null) next = new SortedListNode(data, null);
		else if (data < next.DATA) next = new SortedListNode(data, next);
		else next.insert(data);
	}

	boolean delete(int data) {
		if (next == null) return false;
		if (next.DATA == data) {
			next = next.next;
			return true;
		}
		return (data < next.DATA) ? false : next.delete(data);
	}

	SortedListNode search(int data) {
		if (this.DATA == data) return this;
		else return (next == null || data < next.DATA) ? null : next.search(data);
	}

	void printList() {
		if (next == null) return;
		System.out.print(", " + next.DATA);
		next.printList();
	}
}
