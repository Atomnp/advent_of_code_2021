mappings=[]
def foo(left,num,length,compare_to,diff):
    for i in left.split():
        if len(i)==length and len(set(i+mappings[compare_to]))==length+diff and "".join(sorted(i)) not in mappings:
            mappings[num]="".join(sorted(i))

if __name__=="__main__":
    with open("./Day8/input.txt","r") as f:
        lines=f.read().splitlines()
        right=[line.split(" | ")[1] for line in lines]
        left=[line.split(" | ")[0] for line in lines]
        count=0
        for line in lines:
            mappings=[-1 if x!=8 else "abcdefg" for x in range(10)]   
            left,right=line.split(" | ")
            
            foo(left,1,2,8,5)
            foo(left,4,4,8,3)
            foo(left,7,3,8,4)

            foo(left,6,6,7,1)
            foo(left,0,6,4,1)
            foo(left,9,6,8,1)
            foo(left,3,5,7,0)
            foo(left,5,5,6,1)
            foo(left,2,5,8,2)

            count+=int("".join([str(mappings.index("".join(sorted(i)))) for i in right.split()]))
        print(count)
        


            



