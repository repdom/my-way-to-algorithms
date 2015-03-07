def insertion_sort(lst):
	for index in range(1,len(lst)):
		key = lst[index]
		i = index

		while i>0 and lst[i-1]>key:
			lst[i] = lst[i-1]
			i = i-1
		lst[i] = key
	return lst

def main ():
	lst = [2,5,3,4,6,1]
	return insertion_sort(lst)

if __name__ == "__main__":
    print main()