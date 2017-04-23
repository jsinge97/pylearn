def lists_demo():
	str_to_list = list("hello") # list() can take an iterable
	res = [x * 5 for x in "chili"]
	print res
	abs_arr = list(map(abs, [-1, 0, 1, -2]))
	print abs_arr
	str_to_list[0:2] = ["j", "e"]
	print str_to_list
	# sorting lists
	a = [1, 2, 3]
	print sorted(a) # check this method
	# print str_to_list.sort(key=str.lower)

	# can also use a list comprehension to change the values
	# before sorting

	a = sorted([x + 1 for x in a], reverse=True)
	print a

def dict_demo():
	# if you want to order dict, maybe better to sort keys and then do it?

	test = {'Josh': 0, 'Simar': 4, 'Aneesh': 59}

	print test.items()

    # use dicts for sparse data arrays where you don't

    new_test = {(2, 3, 4): True}

    # test for determining if key is in

    if 'Josh' in test:
        print "josh in test"

        

def main():
	# lists_demo()
	dict_demo()

main()