# python3


def build_heap(data):
    n=len(data)
    swaps=[]
    for i in range(n//2,-1,-1):
        while True:    
            val=2*i+1
            if val>=len(data)or data[i]<data[val]:
                break
            if val+1<len(data)and data[val]>data[val+1]:
                val=val+1
            swaps.append([i,val])
            data[val],data[i]=data[i],data[val] 
            i=val        
    return swaps      

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    check=input()
    if(check.startswith("I")):
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    if(check.startswith("F")):
        fname=input()
        path="/home/runner/work/convert-array-into-heap-KristiansPriede221RDB394/convert-array-into-heap-KristiansPriede221RDB394/tests/"
        ptf=path+fname
        with open (ptf,'r')as file:
            line=file.readlines()
            n=int(line[0])
            data=list(map(int,line[1].split(' ')))

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    if(len(swaps)<=109):   
        for i,j in swaps:
            print(i,j)


if __name__ == "__main__":
    main()
