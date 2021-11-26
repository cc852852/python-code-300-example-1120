# 问题描述：根据N名运动员得分，找到相对等级和获得最高分前3名的人，分别获得金牌、银牌、铜牌。N为整数，并且不超过10000
# 所有运动员成绩独一无二
# 问题示例：输入[5,4,3,2,1]，输出['Gold Medal','Silver Medal','bronze Medal','4',,5]
class Solution:
    # 参数nums：证书列表
    # 返回列表
    def findRelativeRanks(self,nums):
        score={}
        for i in range(len(nums)):
            score[nums[i]]=i
        sortedScore = sorted(nums,reverse=True)
        answer=[0]*len(nums)
        for i in range(len(sortedScore)):
            res = str(i+1)
            if i==0:
                res='Gold Medal'
            if i==1:
                res='Silver Medal'
            if i==2:
                res='Bronze Medal'
            answer[score[sortedScore[i]]] = res
        return answer
#主函数
if __name__ == '__main__':
    num=[5,4,3,2,1]
    s=Solution()
    print('输入：',num)
    print('输出：',s.findRelativeRanks(num))
