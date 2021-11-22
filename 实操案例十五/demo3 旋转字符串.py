# 给定一个字符串（以字符数组的形式）和一个偏移量，根据偏移量原理从做向右旋转字符串
# 输入str="abcdefg",offset=3,输出"efgabcd"
class Solution:
    # 参数s：字符列表
    # 参数offset：整数
    # 返回值 无
    def rotateString(self,s,offset):
        if len(s)>0:
            offset = offset % len(s)
        temp = (s+s)[len(s) - offset : 2 * len(s) - offset]
        for i in range(len(temp)):
            s[i] = temp[i]

if __name__ == '__main__':
    s=['a','b','c','d','e','f','g']
    offset=3
    solution=Solution()
    solution.rotateString(s,offset)
    print('输出：',s)
