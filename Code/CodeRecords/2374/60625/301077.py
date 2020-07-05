import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Set;

public class Main {

	public static void main(String[] args) {
		int[]data= {1,1,2,2,2,3,3,6,6,66,6,6,6};
		int[]result=get(data);
		
		
		
	}

	private static int[] get(int[] data) {
		HashMap<Integer, Integer> h=new HashMap<>();
		for (int i = 0; i < data.length; i++) {
			if (h.get(data[i])==null) {
				h.put(data[i], 1);
			}else {
				h.put(data[i],h.get(data[i])+1);
			}
		}
		
		Set<Entry<Integer, Integer>> keySet = h.entrySet();
		 List<Map.Entry<Integer, Integer>> infoIds = new ArrayList<>(keySet);
		Collections.sort(infoIds, new Comparator<Map.Entry<Integer, Integer>>() {
			@Override
			public int compare(Map.Entry<Integer, Integer> o1, Map.Entry<Integer, Integer> o2) {

				// o1.getValue() - o2.getValue() 升序
				// o2.getValue() - o1.getValue() 降序
				return (o2.getValue() - o1.getValue());

				// o1.getKey()).toString().compareTo(o2.getKey() 升序
				// o2.getKey()).toString().compareTo(o1.getKey() 降序
				// return (o1.getKey()).toString().compareTo(o2.getKey());
			}
		});
		int a=0;
		 for (int i = 0; i < infoIds.size(); i++) {
	           
	            for (int j = 0; j < infoIds.get(i).getValue(); j++) {
	            	Integer id = infoIds.get(i).getKey();
	            	System.out.print(id+" ");
				}
	            
	    }

		return null;
	}
	
}

