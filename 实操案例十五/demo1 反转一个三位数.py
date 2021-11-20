class Soluthon:
    # 参数number:一个三位数
    #返回值：反转后的数字
    def reverseInteger(self,number): # 这里体现命名的科学性
        bai=int(number/100)
        shi=int(number%100/10)
        ge=int(number%10)
        return (ge*100+shi*10+bai)

if __name__ == '__main__':
    solution=Soluthon()
    num=int(input('请输入一个三位数：'))
    ans=solution.reverseInteger(num)
    print('输入：',num)
    print('输出：',ans)