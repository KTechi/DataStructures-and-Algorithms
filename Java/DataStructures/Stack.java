public class Stack {
	private int[] array;
	private int pointer;
	
	public Stack(int size) {
		array = new int[size];
		pointer = 0;
	}
	
	public void push(int data) throws StackException {
		if (isFull()) throw new StackException("This stack is full.");
		array[pointer++] = data;
	}
	
	public int pop() throws StackException {
		if (isEmpty()) throw new StackException("This stack is empty.");
		return array[--pointer];
	}
	
	public int peek() throws StackException {
		if (isEmpty()) throw new StackException("This stack is empty.");
		return array[pointer - 1];
	}
	
	public boolean isEmpty() {
		return pointer == 0;
	}
	
	public boolean isFull() {
		return pointer == array.length;
	}
	
	public void printStack() {
		if (isEmpty()) System.out.print("[null");
		else System.out.print("[" + array[0]);
		
		for (int i = 1; i < pointer; i++) System.out.print(", " + array[i]);
		
		System.out.print("]\n");
	}
}


class StackException extends RuntimeException {
	private static final long serialVersionUID = 1L;
	
	StackException(String str) {
		super(str);
	}
}