public class List {
	private ListNode head;

	public List() {
		head = null;
	}

	public List(int data) {
		head = new ListNode(data, null);
	}

	public void addToHead(int data) {
		head = new ListNode(data, head);
	}

	public void addToTail(int data) {
		if (head == null) head = new ListNode(data, null);
		else head.addToTail(data);
	}

	public boolean delete(int data) {
		if (head == null) return false;
		if (head.getValue() == data) {
			head = head.getNext();
			return true;
		}
		return head.delete(data);
	}

	public ListNode search(int data) {
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


class ListNode {
	private final int DATA;
	private ListNode next;

	ListNode(int data, ListNode next) {
		this.DATA = data;
		this.next = next;
	}

	int getValue() {
		return DATA;
	}

	ListNode getNext() {
		return next;
	}

	void addToTail(int data) {
		if (next == null) next = new ListNode(data, null);
		else next.addToTail(data);
	}

	boolean delete(int data) {
		if (next == null) return false;
		if (next.DATA == data) {
			next = next.next;
			return true;
		}
		return next.delete(data);
	}

	ListNode search(int data) {
		if (this.DATA == data) return this;
		else return (next == null) ? null : next.search(data);
	}

	void printList() {
		if (next == null) return;
		System.out.print(", " + next.DATA);
		next.printList();
	}
}
