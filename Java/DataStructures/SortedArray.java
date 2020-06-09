public class SortedArray {
	private int[] array;
	private int top;
	
	public SortedArray(int size) {
		array = new int[size];
		top = 0;
	}
	
	public void insert(int data) throws SortedArrayException {
		if (isFull()) throw new SortedArrayException("This array is full.");
		if (isEmpty()) array[top] = data;
		else insert(data, findInsertIndex(data, 0, top));
		top++;
	}
	
	private void insert(int data, int index) {
		for (int i = top; index < i;) array[i] = array[--i];
		array[index] = data;
	}
	
	private int findInsertIndex(int data, int left, int right) {
		int mid = (left + right) / 2;
		
		if (mid == 0) return (data < array[0]) ? 0 : 1;
		if (array[mid-1] < data && data < array[mid]) return mid;
		if (mid == left) return right;
		
		return (array[mid] < data) ? findInsertIndex(data, mid, right) : findInsertIndex(data, left, mid);
	}
	
	public boolean delete(int data) {
		int n = findDeleteIndex(data, 0, top - 1);
		if (n == -1) return false;
		delete(data, n);
		top--;
		return true;
	}
	
	private void delete(int data, int index) {
		for (int i = index; i < top - 1;) array[i] = array[++i];
	}
	
	private int findDeleteIndex(int data, int left, int right) {
		int mid = (left + right) / 2;
		
		if (array[mid] == data) return mid;
		if (left == mid) return (array[right] == data) ? right : -1;
		
		return (array[mid] < data) ? findDeleteIndex(data, mid, right) : findDeleteIndex(data, left, mid);
	}
	
	public boolean search(int data) {
		if (isEmpty()) return false;
		return search(data, 0, top - 1);
	}
	
	private boolean search(int data, int left, int right) {
		int mid = (left + right) / 2;
		
		if (array[mid] == data) return true;
		if (left == mid) return array[right] == data;
		
		return (array[mid] < data) ? search(data, mid, right) : search(data, left, mid);
	}
	
	public boolean isEmpty() {
		return top == 0;
	}
	
	public boolean isFull() {
		return top == array.length;
	}
	
	public void printArray() {
		if (isEmpty()) System.out.print("[null");
		else System.out.print("[" + array[0]);
		
		for (int i = 1; i < top; i++) System.out.print(", " + array[i]);
		
		System.out.print("]\n");
	}
}


class SortedArrayException extends RuntimeException {
	private static final long serialVersionUID = 1L;
	
	SortedArrayException(String str) {
		super(str);
	}
}