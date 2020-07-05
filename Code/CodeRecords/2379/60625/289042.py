class Solution:
    def isRobotBounded(self, instruction):
        '''

        :param instruction: str
        :return: bool
        '''
        x, y = 0, 0
        direction = 90
        for j in range(4):
            for i in range(len(instruction)):
                if instruction[i] == 'L':
                    if direction == 270:
                        direction = 0
                    else:
                        direction += 90
                if instruction[i] == 'R':
                    if direction == 0:
                        direction = 270
                    else:
                        direction -= 90
                if instruction[i] == 'G':
                    if direction == 90:
                        y += 1
                    if direction == 180:
                        x -= 1
                    if direction == 270:
                        y -= 1
                    if direction == 0:
                        x += 1
        if x == 0 and y == 0:
            return True
        else:
            return False


t=Solution()
print(t.isRobotBounded(input()))