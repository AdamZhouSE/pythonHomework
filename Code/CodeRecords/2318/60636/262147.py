public class BiggestSubBSTInTree {
	public static class Node {
		public int value;
		public Node left;
		public Node right;

		public Node(int value) {
			this.value = value;
		}
	}

	public static class ReturnData {
		public int size;
		public Node head;
		public int min;
		public int max;

		public ReturnData(int size, Node head, int min, int max) {
			this.size = size;
			this.head = head;
			this.min = min;
			this.max = max;
		}
	}

	public static ReturnData process(Node head) {
		if (head == null) {
			return new ReturnData(0, null, Integer.MIN_VALUE, Integer.MAX_VALUE);
		}
		ReturnData leftInfo = process(head.left);
		ReturnData rightInfo = process(head.right);

		int includeItSelf = 0;
		if (leftInfo.head == head.left && rightInfo.head == head.right && head.value > leftInfo.max
				&& head.value < rightInfo.min) {
			includeItSelf = leftInfo.size + 1 + rightInfo.size;
		}

		int p1 = leftInfo.size;
		int p2 = rightInfo.size;
		int maxSize = Math.max(Math.max(p1, p2), includeItSelf);

		Node maxHead = p1 > p2 ? leftInfo.head : rightInfo.head;
		if (maxSize == includeItSelf) {
			maxHead = head;
		}

		return new ReturnData(maxSize, maxHead, Math.min(Math.min(leftInfo.min, rightInfo.min), head.value),
				Math.max(Math.min(leftInfo.min, rightInfo.min), head.value));
	}
}
