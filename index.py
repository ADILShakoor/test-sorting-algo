
def insertion_sort(my_list):
    for i in range(1,len(my_list)):
        temp=my_list[i]
        j=i-1
        while temp<my_list[j] and j > -1:
            my_list[j+1]=my_list[j]
            my_list[j]=temp
            j-=1
    return my_list

print(insertion_sort([4,2,5,6,9]))
# print(insertio_sort('ali',"hasbs","jajjs","bsshs"))

def srt_sort():
    string=["apple",'banana','zbbaj','cjdnn']
    # for i in range(1,len(string)):
    string.sort()