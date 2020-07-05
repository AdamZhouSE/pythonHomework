class Solution {
public:
    int result = 0;
	int reversePairs(vector<int>& nums) {
		if (nums.size() <= 1) {
			return 0;
		}
		vector<int> mergeVec(nums.size());
		sort(0, nums.size() - 1, nums, mergeVec);//归并排序
		return result;
	}
    //处理nums[left, right]
	void sort(int left, int right, vector<int> & data, vector<int> &mergeVec) {
		if (left >= right){
            return;
        }
        int mid = (left + right) / 2;
        sort(left, mid, data, mergeVec);//第一步：处理 [left, mid] （递归）
        sort(mid + 1, right, data, mergeVec);//第二步：处理[mid + 1, right] （递归）
        int i = left;
        int j = mid + 1;
        //第三步：计算左段各个元素在右端构成的 “重要翻转对”(由于排序左（右）段已经计算了左（右）段内产生的“重要翻转对”，所以这里只需要计算两个段之间的“重要翻转对”)
        while (j < right + 1 && i < mid + 1) {
            if ((long)data[i] > (long)2 * data[j]) {
                result += (mid + 1 - i);
                j += 1;
            }
            else {
                i += 1;
            }
        }
        //第四步：有序合并左右两段
        merge(left, right, data, mergeVec);//data中[left, mid]和[mid + 1, right]两段进行合并到result中[left, right]
        //复制回data
        for (int i = left; i <= right; i++) {
            data[i] = mergeVec[i];
        }
	}
    //将data中[left, mid]和[mid + 1, right]两段进行合并到result中[left, right]
	void merge(int left, int right, vector<int> & data, vector<int> &mergeVec) {
		int mid = (left + right) / 2;
		int oneBegin = left;//第一段
		int twoBegin = mid + 1;//第二段
		int mergeIndex = left;//合并段
        //将较小者写入合并段
		while (oneBegin <= mid && twoBegin <= right) {
			if (data[oneBegin] <= data[twoBegin]) {
				mergeVec[mergeIndex++] = data[oneBegin++];
			}
			else {
				mergeVec[mergeIndex++] = data[twoBegin++];
			}

		}
        //下面的循环只会执行一个
		while (oneBegin <= mid) {
			mergeVec[mergeIndex++] = data[oneBegin++];
		}
		while (twoBegin <= right) {
			mergeVec[mergeIndex++] = data[twoBegin++];
		}
	}
};
