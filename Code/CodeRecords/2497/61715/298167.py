class Solution :
    def kcars(self):
        n = int(input())
        position = list(input())
        speed = list(input())
        difPosition = []
        for i in position :
            difPosition.append(n-i)
        time = []
        for i in range(difPosition.__len__()) :
            time.append(difPosition[i]/speed[i])
        for i in range(position.__len__()-1) :
            for o in range(i+1, position.__len__()) :
                if position[i] < position[o] :
                    position[i], position[o] = position[o], position[i]
                    time[i], time[o] = time[o], [i]
        i = 0
        while i < position.__len__() - 1:
            o = i + 1
            while o < position.__len__() :
                if (position[o] < position[i]) and (time[o] <= time[i]) :
                    del position[o]
                    del time[o]
                else:
                    o += 1
            i += 1
        print(position.__len__())
so = Solution()
so.kcars()