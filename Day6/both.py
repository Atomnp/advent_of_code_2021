memo={}
def solve(day_remaining,time_for_breed):
    if day_remaining<=time_for_breed:
        return 1
    if (day_remaining,time_for_breed) in memo:
        return memo[day_remaining,time_for_breed]
    else:
        res=solve(day_remaining-time_for_breed-1,6)+solve(day_remaining-1-time_for_breed,8)
        memo[(day_remaining,time_for_breed)]=res
        return res

if __name__ =='__main__':
    with open('./Day6/input.txt', 'r') as f:
        lines = [int(a.strip()) for a in f.readline().split(',')]

    first=sum([solve(80,int(x)) for x in lines])
    second=sum([solve(256,int(x)) for x in lines])
    print(first)
    print(second)
