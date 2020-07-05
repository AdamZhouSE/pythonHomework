private static int[][] merge(int[][] intervals) {
        //边界判断
        if (intervals.length <= 1) {
            return intervals;
        }

        //先按起点位置进行排序
        Arrays.sort(intervals, Comparator.comparingInt(o -> o[0]));

        //利用list存储合并好的区间
        List<int[]> result = new ArrayList<>();
        //初始时将第一个区间放入list中
        result.add(intervals[0]);
        //记录上一合并好的区间在list中的位置
        int last = 0;
        //遍历并合并后面各区间
        for (int i = 1; i < intervals.length; i++) {
            //上一合并好的区间的起点和终点
            int lastStart = result.get(last)[0];
            int lastEnd = result.get(last)[1];
            //当前要合并的区间的起点和终点
            int start = intervals[i][0];
            int end = intervals[i][1];
            //如果左边重合
            if (lastStart == start) {
                if (end > lastEnd) {
                    result.set(last, new int[] {start, end});
                }
            } else {    //如果左边不重合
                if (start > lastEnd) {
                    result.add(new int[] {start, end});
                    last++;
                } else {
                    if (end > lastEnd) {
                        result.set(last, new int[] {lastStart, end});
                    }
                }
            }
        }

        return result.toArray(new int[0][]);
    }
