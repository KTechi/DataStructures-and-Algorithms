public class Queue {
	private int[] array;
	private int top, bottom;
	
	public Queue(int size) {
		array = new int[size+1];
		top = bottom = 0;
	}
	
	public void enqueue(int data) throws QueueException {
		if (isFull()) throw new QueueException("This queue is full.");
		array[top] = data;
		top = (top + 1) % array.length;
	}
	
	public int dequeue() throws QueueException {
		if (isEmpty()) throw new QueueException("This queue is empty.");
		bottom = (bottom + 1) % array.length;
		return array[(bottom - 1 + array.length) % array.length];
	}
	
	public int peek() throws QueueException {
		if (isEmpty()) throw new QueueException("This queue is empty.");
		return array[bottom];
	}
	
	public boolean isEmpty() {
		return top == bottom;
	}
	
	public boolean isFull() {
		return (top + 1) % array.length == bottom;
	}
	
	public void printQueue() {
		if (isEmpty()) System.out.print("[null");
		else System.out.print("[" + array[bottom]);
		
		if (!isEmpty())
			for (int i = (bottom + 1) % array.length; i != top; i = (i + 1) % array.length)
				System.out.print(", " + array[i]);
		
		System.out.print("]\n");
	}
}


class QueueException extends RuntimeException {
	private static final long serialVersionUID = 1L;
	
	QueueException(String str) {
		super(str);
	}
}